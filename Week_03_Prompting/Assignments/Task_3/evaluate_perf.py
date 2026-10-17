"""Measure SQL query execution performance for all Task 2 predictions."""

import csv
import re
import sqlite3
import time
from pathlib import Path


TASK_2_DIR = Path(__file__).resolve().parent.parent / "Task_2"
PREDICTIONS_DIR = TASK_2_DIR / "predictions"
SCHEMA_PATH = TASK_2_DIR / "data" / "restaurants-schema.csv"
DATABASE_PATH = TASK_2_DIR / "data" / "restaurants-db.txt"
MEASUREMENTS_PER_FILE = 10


def sqlite_type(schema_type):
    normalized_type = schema_type.strip().lower()
    if normalized_type.startswith("int"):
        return "INTEGER"
    if normalized_type.startswith(("decimal", "float")):
        return "REAL"
    return "TEXT"


def load_database():
    tables = {}
    with SCHEMA_PATH.open(encoding="utf-8", newline="") as schema_file:
        for table, field, primary_key, _foreign_key, column_type in csv.reader(
            schema_file, skipinitialspace=True
        ):
            table = table.strip()
            field = field.strip()
            if table == "-":
                continue
            tables.setdefault(table, []).append(
                (field, sqlite_type(column_type), primary_key.strip().lower() == "y")
            )

    connection = sqlite3.connect(":memory:")
    for table, columns in tables.items():
        definitions = []
        for field, column_type, primary_key in columns:
            definition = f'"{field}" {column_type}'
            if primary_key:
                definition += " PRIMARY KEY"
            definitions.append(definition)
        connection.execute(f'CREATE TABLE "{table}" ({", ".join(definitions)})')

    with DATABASE_PATH.open(encoding="utf-8") as database_file:
        for line_number, line in enumerate(database_file, start=1):
            match = re.fullmatch(r"([A-Z_]+)\((.*)\)", line.rstrip("\r\n"))
            if match is None:
                raise ValueError(f"Invalid database record on line {line_number}")

            table, values_text = match.groups()
            if table not in tables:
                raise ValueError(f"Unknown table {table!r} on line {line_number}")

            values = next(csv.reader([values_text], skipinitialspace=True))
            columns = tables[table]
            if len(values) != len(columns):
                raise ValueError(
                    f"Expected {len(columns)} values for {table} on line "
                    f"{line_number}, got {len(values)}"
                )

            converted_values = []
            for value, (_field, column_type, _primary_key) in zip(values, columns):
                if column_type == "INTEGER":
                    converted_values.append(int(value))
                elif column_type == "REAL":
                    converted_values.append(float(value))
                else:
                    converted_values.append(value)

            placeholders = ", ".join("?" for _ in columns)
            connection.execute(
                f'INSERT INTO "{table}" VALUES ({placeholders})', converted_values
            )

    return connection


def measure_predictions(predictions_path, connection):
    total_time = 0.0
    query_count = 0
    with predictions_path.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames is None or "predicted_sql" not in reader.fieldnames:
            raise ValueError(
                f"Missing predicted_sql column in {predictions_path}"
            )

        for line_number, row in enumerate(reader, start=2):
            query = row["predicted_sql"]
            start = time.perf_counter()
            try:
                connection.execute(query).fetchall()
            except sqlite3.Error as error:
                raise RuntimeError(
                    f"Could not execute predicted SQL on line {line_number} "
                    f"of {predictions_path}"
                ) from error
            total_time += time.perf_counter() - start
            query_count += 1

    if query_count == 0:
        raise ValueError(f"No predictions found in {predictions_path}")

    return total_time, total_time / query_count, query_count


def measure_predictions_average(predictions_path, connection):
    total_times = []
    query_count = None
    for _ in range(MEASUREMENTS_PER_FILE):
        total_time, _average_time, measured_query_count = measure_predictions(
            predictions_path, connection
        )
        if query_count is None:
            query_count = measured_query_count
        elif measured_query_count != query_count:
            raise ValueError(
                f"Prediction count changed between measurements for "
                f"{predictions_path}"
            )
        total_times.append(total_time)

    average_total_time = sum(total_times) / MEASUREMENTS_PER_FILE
    return average_total_time, average_total_time / query_count, query_count


def main():
    csv.field_size_limit(1_000_000_000)
    prediction_files = sorted(PREDICTIONS_DIR.glob("*.csv"))
    if not prediction_files:
        raise ValueError(f"No prediction CSV files found in {PREDICTIONS_DIR}")

    connection = load_database()
    try:
        for predictions_path in prediction_files:
            total_time, average_time, query_count = measure_predictions_average(
                predictions_path, connection
            )
            print(predictions_path.name)
            print(f"  Measurements: {MEASUREMENTS_PER_FILE}")
            print(f"  Queries: {query_count}")
            print(f"  Average total execution time: {total_time:.6f} seconds")
            print(
                "  Average execution time of single query: "
                f"{average_time:.6f} seconds"
            )
    finally:
        connection.close()


if __name__ == "__main__":
    main()
