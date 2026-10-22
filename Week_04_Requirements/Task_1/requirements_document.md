# Software Requirements Specification

## Priority Scale

- **MUST**: Required for the system to be acceptable.
- **SHOULD**: Important, but the system may operate without it.
- **COULD**: Desirable optional functionality.
- **WONT**: Explicitly excluded or deferred.

## Requirements

### REQ-001: Material volume reporting at any point in time

The system shall provide a report of the volume of materials in a specified library as of any point in time, so users can support board reporting, collection management, and historical comparisons.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines014_material_volume.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> The system should provide the ability to report on the volume of material in a given library at any point in time.
> Ability to report on the volume of material in a given library at any point in time.

### REQ-002: Material volume status breakdown and total

The material volume report shall count new acquisitions, checked-in items, and checked-out items separately and also provide their aggregate total, reflecting a complete definition of volume across item states.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines014_material_volume.eml`

**Evidence:**
> The volume should include: 1. New acquisitions ... 2. Items on the shelf (checked in) 3. Items out in circulation (checked out)
> I think Maria is asking for all three counts separately plus a total.

### REQ-003: Material volume category breakdown (including holds, adult fiction, and board books)

The material volume report shall support breaking down volume into categories including total items in the library, number of holds, number of adult fiction, and number of board books, and it shall be extensible to support additional categories.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines014_material_volume.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> The report should allow breaking down volume in categories such as: Total items in library, Number of holds, Number of adult fiction, Number of board books, Other customizable categories
> The report should allow breaking down volume in categories such as: total items in library, number of holds, number of adult fiction, number of board books, etc.

### REQ-004: Customizable material volume categories

Users shall be able to customize the categories used in material volume reports so different libraries can use different breakdown definitions.

**Priority:** SHOULD

**Traceability:**
- `conversations/conv_pines014_material_volume.eml`

**Evidence:**
> Can we make the categories customizable? Different libraries might want different breakdowns.

### REQ-005: Historical material volume date filtering

The system shall allow date filters for material volume reporting to report volume at historical points in time, enabling historical comparisons rather than only current reporting.

**Priority:** SHOULD

**Traceability:**
- `conversations/conv_pines014_material_volume.eml`

**Evidence:**
> We can also add date filters - volume at any point in time, not just current. This would be useful for historical comparisons.

### REQ-006: System-wide branch capacity overview

The system shall provide an interface that shows the capacity of all branches at once and includes a high-level summary view across all branches and key metrics for at-a-glance comparison.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines015_capacity_interface.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> The system should provide an interface showing the capacity of all branches.
> The system should provide an interface showing the capacity of all branches.
> A high-level summary view (all branches, key metrics)

### REQ-007: Capacity branch drilldown

The capacity interface shall allow users to drill down from the high-level summary into individual branch details so users can investigate specific branches.

**Priority:** SHOULD

**Traceability:**
- `conversations/conv_pines015_capacity_interface.eml`

**Evidence:**
> Ability to drill down into individual branches

### REQ-008: Capacity sorting and filtering

The capacity interface shall support sorting and filtering by region, library type, and current load to help users focus on relevant parts of the multi-location overview.

**Priority:** SHOULD

**Traceability:**
- `conversations/conv_pines015_capacity_interface.eml`

**Evidence:**
> I'd want to be able to sort and filter. By region, by library type, by current load

### REQ-009: Capacity trend reporting

The capacity interface shall display whether branches are growing or shrinking over time to support long-term planning.

**Priority:** SHOULD

**Traceability:**
- `conversations/conv_pines015_capacity_interface.eml`

**Evidence:**
> Can the capacity interface also show trends? Like, is this branch growing or shrinking?

### REQ-010: Capacity CSV export

The capacity interface shall allow users to export results to CSV so directors can consume the data in spreadsheets.

**Priority:** SHOULD

**Traceability:**
- `conversations/conv_pines015_capacity_interface.eml`

**Evidence:**
> And export to CSV for the directors who want spreadsheets.

### REQ-011: Shelf space utilization comparison by genre and format

The system shall provide a shelf space utilization report that, for each genre and format of material, compares the percentage of total circulations, the percentage of the collection, and the percentage of total shelf space.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines016_shelf_space.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> For each genre and format of material, compare: 1. Percentage of total circulations 2. Percentage of the collection 3. Percentage of total shelf space
> For each genre and format of material, ability to compare: - The percentage of total circulations - The percentage of the collection - The percentage of total shelf space

### REQ-012: Shelf space utilization report scope (library and system levels)

The shelf space utilization report shall be available at both the per-library level and the system-wide level so managers can view local and consolidated results.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines016_shelf_space.eml`

**Evidence:**
> The report should be able to run per library and per system.

### REQ-013: Shelf space utilization date-range filtering

The shelf space utilization report shall support filtering by date range to enable comparisons across periods (e.g., Q1 vs. Q2).

**Priority:** SHOULD

**Traceability:**
- `conversations/conv_pines016_shelf_space.eml`

**Evidence:**
> Can we also filter by date range? Like, what was the shelf space utilization in Q1 vs. Q2?

### REQ-014: Side-by-side shelf space comparison view

The system should provide a comparison view that shows each library's shelf space utilization breakdown side by side to help identify outliers across libraries.

**Priority:** COULD

**Traceability:**
- `conversations/conv_pines016_shelf_space.eml`

**Evidence:**
> Can we also include a "comparison" view that shows each library's breakdown side by side?

### REQ-015: Shelf space estimation when direct data is unavailable

The system shall estimate shelf space by item dimensions and, when necessary, use item count as a proxy when direct shelf-space data is unavailable.

**Priority:** SHOULD

**Traceability:**
- `conversations/conv_pines016_shelf_space.eml`

**Evidence:**
> We'd need to estimate based on item dimensions or use item count as a proxy.

### REQ-016: Batch item transfer utility

The system shall provide a utility for transferring batches of items between branches to support mobile libraries, outreach programs, warehouses, and collection balancing.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines018_item_transfer.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> I need a utility for transferring batches of items between branches.
> System should provide a utility for transferring batches of items between branches.

### REQ-017: Transfer candidate query

The transfer utility shall allow users to query for candidate materials to use as the starting point for a batch transfer.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines018_item_transfer.eml`

**Evidence:**
> Query for candidate materials

### REQ-018: Saved transfer candidate-selection queries

The transfer utility shall allow users to save candidate-selection queries and reuse them for repeated transfer workflows.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines018_item_transfer.eml`

**Evidence:**
> Save queries for repeated use
> The "save queries for repeated use" is crucial. We do this monthly

### REQ-019: Manual transfer selection from query results

The transfer utility shall allow users to manually select individual titles or items from the query results so they can transfer a subset of the candidate set.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines018_item_transfer.eml`

**Evidence:**
> Manually select titles from query results
> I should be able to check boxes and select which ones to include.

### REQ-020: Update item locations during transfer

The transfer utility shall change the location records of selected items to a new destination location as one supported transfer mechanism.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines018_item_transfer.eml`

**Evidence:**
> Change records of selected items to new location
> Batch update of location field

### REQ-021: Printable transfer pull lists

The transfer utility shall generate printable pull lists for selected items to support physical retrieval of material for transfer.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines018_item_transfer.eml`

**Evidence:**
> Mechanisms: changing location field, generating pull lists
> Pull list generation - create a printable list of items to be moved.

### REQ-022: Transfer preview and confirmation before applying changes

The transfer utility shall show a preview of proposed changes and require user confirmation before applying them, including enabling staff to see the number of items and the destination before execution.

**Priority:** SHOULD

**Traceability:**
- `conversations/conv_pines018_item_transfer.eml`

**Evidence:**
> The utility should show a preview before making changes.
> Confirm?

### REQ-023: Transfer undo support

The transfer utility should provide an undo function to protect against accidental transfers.

**Priority:** SHOULD

**Traceability:**
- `conversations/conv_pines018_item_transfer.eml`

**Evidence:**
> And we need an undo function!

### REQ-024: Transfer permissions by authorized roles

The system shall restrict item transfers to authorized roles such as managers, administrators, or transfer coordinators so not every staff member can perform transfers between branches.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines018_item_transfer.eml`

**Evidence:**
> Not every staff member should be able to transfer items between branches. This should be limited to certain roles

### REQ-025: Transfer history tracking per item

The system shall track transfer history for each item so users can identify items transferred repeatedly (e.g., how many times in a given period).

**Priority:** SHOULD

**Traceability:**
- `conversations/conv_pines018_item_transfer.eml`

**Evidence:**
> Can we track transfer history? Like, "this item has been transferred 5 times in the past year."

### REQ-026: Automatic transfer reversion

The system shall revert transferred items back to their original location after a configured period or when configured criteria are met to support temporary transfers.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines018_item_transfer.eml`

**Evidence:**
> Revert items to original location after a set period of time
> Auto-revert mechanism ... reverts them based on time or status criteria.

### REQ-027: Event-based transfer reversion criteria

The system should support event-based transfer reversion, including reverting when an item status changes to "returned" and when an item is checked out at the destination.

**Priority:** SHOULD

**Traceability:**
- `conversations/conv_pines018_item_transfer.eml`

**Evidence:**
> Revert when item status changes to "returned"
> Revert when item is checked out at the destination

### REQ-028: Printable transfer transit labels or barcodes

The transfer utility should generate printable transit labels or barcodes for transferred items to support physical transit processing.

**Priority:** SHOULD

**Traceability:**
- `conversations/conv_pines018_item_transfer.eml`

**Evidence:**
> Can we generate transit labels? Like, printable barcodes for the items being transferred?

### REQ-029: Transfer delay and issue alerts

The system should notify users when a transfer is delayed or has issues so staff can respond to exceptions.

**Priority:** COULD

**Traceability:**
- `conversations/conv_pines018_item_transfer.eml`

**Evidence:**
> Can we set up alerts? If an item transfer is delayed or has issues, notify me.

### REQ-030: Transfer audit logging

The system shall log all transfers for audit purposes.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines018_item_transfer.eml`

**Evidence:**
> Logging - track all transfers for audit purposes.

### REQ-031: Missing and damaged items report per branch

The system shall provide reports of missing and damaged items per branch to support inventory audits and collection management.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines019_020_missing_intransit.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> System provides reports of missing and damaged items per branch.
> The system should provide reports of missing and damaged items per branch.

### REQ-032: Missing and damaged item condition notes in reports

The missing and damaged items report should include item condition notes such as water damage or vandalism to help identify causes.

**Priority:** SHOULD

**Traceability:**
- `conversations/conv_pines019_020_missing_intransit.eml`

**Evidence:**
> Can the report include item condition notes? Like "water damage" or "vandalism"?

### REQ-033: Missing and damaged items date-range filtering

The missing and damaged items report should support date-range filtering to enable trending and audit-period reporting.

**Priority:** SHOULD

**Traceability:**
- `conversations/conv_pines019_020_missing_intransit.eml`

**Evidence:**
> The missing/damaged report can include date ranges

### REQ-034: In-transit aging report with configurable threshold

The system shall list items that have been in transit longer than a configurable number of days, with the report available per branch and per system (with a suggested default of seven days).

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines019_020_missing_intransit.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> System generates a list of items in-transit for more than X days (X configurable), per branch and per system.
> X should be configurable, probably 7 days default

### REQ-035: In-transit report merges transit-to and transit-from

The in-transit report shall merge transit-to and transit-from items into a single report so front-line staff do not need separate reports.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines019_020_missing_intransit.eml`

**Evidence:**
> The report merges transit-to and transit-from into one report for ease of front-line staff.

### REQ-036: In-transit report sorting by due date

The in-transit report should support sorting by due date so staff can pursue the oldest items first.

**Priority:** SHOULD

**Traceability:**
- `conversations/conv_pines019_020_missing_intransit.eml`

**Evidence:**
> Can we sort by due date? Front-line staff need to chase the oldest items first.

### REQ-037: Purge candidate identification using customizable criteria

The system shall identify item records for purging using customizable criteria to support weeding workflows.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines021_item_purging.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> I need to identify item records to purge based on customizable criteria.
> The system should provide a utility and reports for identifying item records to purge, based on customizable criteria

### REQ-038: Combined purge criteria with logical conditions

The purging utility shall allow status-based, time-based, and activity-based criteria to be combined using logical conditions (for example, missing status duration AND lack of circulation).

**Priority:** SHOULD

**Traceability:**
- `conversations/conv_pines021_item_purging.eml`

**Evidence:**
> The system should let us combine criteria.
> items with status 'missing' for more than 6 months AND haven't circulated in 2 years

### REQ-039: Batch status conversion report/utility for purging

The system shall provide a report and utility to convert many items from one status to another in batch, including the example of converting missing items to discard/weed.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines021_item_purging.eml`

**Evidence:**
> A report to help convert items from one status to another in batch.
> changing 100 items from "missing" to "discard/weed" at once.

### REQ-040: Last copy report to identify last consortium copies

The system shall provide a last-copy report that identifies the last copy within a selected library or across the entire system, preventing accidental deletion of the last consortium copy and supporting WorldCat updates.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines021_item_purging.eml`
- `interview_cataloging_2009-05-08.txt`

**Evidence:**
> CRITICAL: We need a "last copy report" that identifies our library system's last copies.
> For the last copy report ... we need both views.
> And the last copy report is CRITICAL.

### REQ-041: Volume and copy cleanup (delete volume entries with attached copies and delete orphan records)

The system shall provide a quick method to delete volume entries together with associated copy entries and to delete records with no attached items, supporting cleanup of orphaned catalog records.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines021_item_purging.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> We also need a quick way to delete volume entries along with copy entries, and delete records with no items attached.
> quick effective method of deleting volume entries along with copy entries, as well as records with no items attached

### REQ-042: Purge safety confirmation workflow

The system shall show purge candidates in read-only reports and require a separate confirmation step before performing actual deletions.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines021_item_purging.eml`

**Evidence:**
> Reports show candidates for purging (read-only)
> A separate confirmation step for actual deletions

### REQ-043: Purges audit trail

The system shall maintain an audit trail of all purges, including who purged what and when.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines021_item_purging.eml`

**Evidence:**
> Audit trail for all purges.
> We need to track who purged what and when.

### REQ-044: Deletion tracking for item and patron records by location and system

The system shall count and track deletions of records such as item and patron records by location and by system for auditing and troubleshooting.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines022_deletions.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> We need to be able to count and track record deletions (item records, patron records) per location and per system.
> Ability to count and track record deletions ... per location and per system.

### REQ-045: Deletion audit record attributes

Deletion records shall include record type, record identifier, timestamp, deleting user, and user location to support traceability of deletions.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines022_deletions.eml`

**Evidence:**
> Fields: record_type, record_id, deleted_by, deleted_at, location

### REQ-046: Deletion reporting filters and aggregation

The deletion report shall support aggregation by date range, user, record type, location, and system to enable periodic accountability reporting.

**Priority:** SHOULD

**Traceability:**
- `conversations/conv_pines022_deletions.eml`

**Evidence:**
> We can aggregate by date range, by user, by record type.
> Total deletions per period ... Deletions by type ... Deletions by location

### REQ-047: Track denied deletion attempts

The system should track deletion attempts that were denied so administrators can investigate and troubleshoot blocked actions.

**Priority:** COULD

**Traceability:**
- `conversations/conv_pines022_deletions.eml`

**Evidence:**
> Can we also track attempted deletions that were denied?

### REQ-048: Patron characteristic reporting filters

The system shall allow reports to be filtered and grouped by age range, zip code, county, home branch, patron type, and preferred language to support program planning and collection decisions.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines023_patron_characteristics.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> The system should allow queries and reports to be limited or grouped by various patron characteristics
> including: Age range, Zip code, County of residence, Home branch, Patron type, Preferred language

### REQ-049: Configurable age ranges for patron reports

Patron reports shall support configurable age brackets per report so different programs can define age groupings differently.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines023_patron_characteristics.eml`

**Evidence:**
> The age ranges need to be configurable too.
> Age ranges should be configurable per report

### REQ-050: Combined patron filters with AND/OR logic

Patron reports shall support combining demographic filters using AND and OR logical conditions so users can build compound selections.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines023_patron_characteristics.eml`

**Evidence:**
> Filters can be combined with AND/OR logic

### REQ-051: Include patrons with null optional demographic values

Patron reports shall include patrons with null or missing optional demographic values (with nulls shown) rather than excluding them so results are not misleading.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines023_patron_characteristics.eml`

**Evidence:**
> We should include them in the report (with null values) rather than excluding them

### REQ-052: Inactive patron report for configurable inactivity threshold

The system shall generate a list of patrons with no circulation or electronic activity during a configurable number of preceding days (X), with X being configurable.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines024_inactive_patrons.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> We need a report that shows patrons with no circulation or electronic activity in the last X days. X should be configurable
> The system should generate a list of patrons with no circulation or electronic activity in the last X days (X configurable).

### REQ-053: Inactive patron report aggregation levels

The inactive patron report shall support system, home library, county, and other configured aggregation levels to support different outreach and cleanup scopes.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines024_inactive_patrons.eml`

**Evidence:**
> The list should be configurable to different levels - System, Home Library, County, etc.

### REQ-054: Inactive electronic activity definition

For inactive-patron reporting, electronic activity shall include OPAC/patron account logins, online hold placement, online renewals, and logged digital-resource access (if integrated) so that electronic engagement counts even without physical circulation.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines024_inactive_patrons.eml`

**Evidence:**
> "Electronic activity" should include: 1. Logging into OPAC/patron account 2. Placing holds online 3. Renewing items online 4. Accessing digital collections (if integrated)

### REQ-055: Inactive patron report separate outstanding fines

The inactive patron report shall identify patrons with outstanding fines separately to support different handling of those accounts.

**Priority:** SHOULD

**Traceability:**
- `conversations/conv_pines024_inactive_patrons.eml`

**Evidence:**
> Track inactive patrons who still owe fines separately.

### REQ-056: Inactive patron report exclusions

The inactive patron report shall allow exclusion of patrons based on flags or types, including do-not-disturb, VIP, staff, and communication opt-out, so outreach/cleanup can omit excluded populations.

**Priority:** SHOULD

**Traceability:**
- `conversations/conv_pines024_inactive_patrons.eml`

**Evidence:**
> We should be able to EXCLUDE certain patrons from the inactive report.
> Patrons with "do not disturb" flags ... VIP patrons ... Staff members ... opted out of communications

### REQ-057: Inactive patron report mailing addresses

The inactive patron report shall include current mailing addresses so the report can be used for outreach mailings.

**Priority:** SHOULD

**Traceability:**
- `conversations/conv_pines024_inactive_patrons.eml`

**Evidence:**
> the report needs to include current mailing addresses.

### REQ-058: Inactive patron report CSV export

The inactive patron report shall be exportable in CSV format so it can be uploaded to an outreach system.

**Priority:** SHOULD

**Traceability:**
- `conversations/conv_pines024_inactive_patrons.eml`

**Evidence:**
> the report should be exportable. We upload it to our outreach system.
> Exportable format (CSV)

### REQ-059: Background execution and caching for long-running reports

Long-running reports shall execute in the background and cache results where necessary so report processing does not block interactive usage.

**Priority:** MUST

**Traceability:**
- `conversations/conv_pines024_inactive_patrons.eml`
- `interview_sysadmin_2009-05-10.txt`

**Evidence:**
> We should run it as a background report and cache results.
> We need to make sure reports can be queued and processed in the background.

### REQ-060: User-friendly query interface across record types

The system shall provide a user-friendly query interface for bibliographic, item, patron, transaction, and financial records so staff can perform ad hoc reporting across relevant record types.

**Priority:** MUST

**Traceability:**
- `email_report_features.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> We need a user-friendly interface for designing queries against all record types.
> The system should provide a user-friendly interface for designing queries against all record types

### REQ-061: Query field/value selection and Boolean/regex operators

The query tool shall allow users to select query fields, choose values from picklists, use regular expressions, and apply Boolean operators so queries can address reporting needs beyond basic limitations.

**Priority:** MUST

**Traceability:**
- `email_report_features.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> select fields to query, select values from picklists, use regular expressions from a dropdown, and use Boolean operators

### REQ-062: Report templates with administrator-defined limits

Administrators shall be able to create report templates that staff can run as-is or modify within administrator-defined limits to provide consistent reporting while retaining administrative control.

**Priority:** MUST

**Traceability:**
- `email_report_features.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> Admins need to create report templates that are available to staff.
> Administrators should be able to limit which filters and display fields can be altered

### REQ-063: Clone report templates

Authorized users shall be able to clone existing report templates into new variants so they can create related reports without modifying the original template.

**Priority:** SHOULD

**Traceability:**
- `email_report_features.eml`

**Evidence:**
> We also need the ability to "clone" reports - take an existing template and create a new one based on it.

### REQ-064: Fine-grained report permissions

The system shall provide fine-grained permissions controlling who can create, clone, run, and modify reports so capabilities vary by role.

**Priority:** MUST

**Traceability:**
- `email_report_features.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> We need distinct, fine-grained permission levels limiting who can create and clone reports.
> The system should provide distinct, fine-grained permission levels

### REQ-065: Shared folders for report access control

Administrators shall be able to create shared folders that allow or disallow staff from running specified reports to support organized and controlled access.

**Priority:** SHOULD

**Traceability:**
- `email_report_features.eml`

**Evidence:**
> Admins can create shared folders to allow or disallow staff from running specific reports

### REQ-066: Role-based security groups/roles for permissions

User rights and privileges shall be controlled through security groups or roles assignable to individuals, workgroups, and arbitrary staff groups to support role-based permission administration.

**Priority:** MUST

**Traceability:**
- `email_staff_login.eml`
- `interview_sysadmin_2009-05-10.txt`
- `early_draft_srs_galecia.txt`

**Evidence:**
> User rights and privileges controlled through security groups/roles.
> The system needs to be controlled through security groups and/or "roles."

### REQ-067: Optional streamlined staff login (e.g., card/RFID swipe)

The system shall support optional streamlined staff login methods such as card or RFID badge swipe to reduce service delays while remaining optional.

**Priority:** SHOULD

**Traceability:**
- `email_staff_login.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> The system supports (but does not require) streamlined staff login methods, e.g. card swipe
> The system should support streamlined methods of logging into terminals.

### REQ-068: Username/password staff login fallback

The system shall support individual username-and-password staff login as an alternative to streamlined login so traditional authentication remains available.

**Priority:** MUST

**Traceability:**
- `email_staff_login.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> We also need to support the traditional username/password method
> traditional username/password should also be available as a fallback.

### REQ-069: Individual staff accountability for authenticated sessions

The system shall identify the individual staff member authenticated through any login method for audit purposes so card-based login still results in individual accountability.

**Priority:** MUST

**Traceability:**
- `email_staff_login.eml`

**Evidence:**
> The system must track WHICH staff member is logged in for audit purposes.

### REQ-070: Predefined board and executive reports

The system shall provide predefined board and executive reports containing circulation, check-in, holds, and usage statistics to support board presentations and annual reporting.

**Priority:** MUST

**Traceability:**
- `email_report_features.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> Pre-defined reports for library boards with basic statistics.
> Activity reports should indicate traffic and volume of use

### REQ-071: Cross-tabulated activity reporting dimensions

Activity reports shall support cross-tabulation by terminal, branch, system, hour, patron age range, patron type, and patron location.

**Priority:** MUST

**Traceability:**
- `email_report_features.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> Cross-tabulated per terminal, per branch, per system, per hour, per age range, per patron type, per patron location.

### REQ-072: Display query criteria with report results

Report results shall display the query selections and criteria used to generate them so users can verify report scope and reproduce results.

**Priority:** MUST

**Traceability:**
- `email_report_features.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> System provides query selections along with results.
> The system should provide the query selections along with the results

### REQ-073: Report queue visibility and status

Users shall be able to see a submitted report’s queue position, number of reports ahead, submission time, and status, where status includes waiting, running, completed, and failed.

**Priority:** MUST

**Traceability:**
- `email_report_features.eml`
- `evergreen_reference_2009.txt`

**Evidence:**
> They need to see: That their report is in the queue; How many reports are ahead; When their report was submitted; Status (waiting, running, completed, failed)

### REQ-074: Prioritize reports in the queue

Authorized users shall be able to prioritize important reports in the report queue so important reports can run ahead of other queued reports.

**Priority:** SHOULD

**Traceability:**
- `email_report_features.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> Important reports can jump queue.
> Ability to prioritize certain types of reports

### REQ-075: Cancel scheduled or running reports

Users shall be able to cancel scheduled or currently running reports to stop unnecessary or erroneous report executions.

**Priority:** SHOULD

**Traceability:**
- `early_draft_srs_galecia.txt`
- `meeting_tech_subcommittee_2009-06-30.txt`

**Evidence:**
> Ability to cancel a report that has already been scheduled to run or is currently running
> The ability to cancel a scheduled or running report is technically feasible

### REQ-076: Report scheduling frequencies

The system shall support scheduling reports with frequencies including ASAP, hourly, daily, weekly, monthly, and yearly to enable recurring and immediate report execution.

**Priority:** MUST

**Traceability:**
- `early_draft_srs_galecia.txt`
- `evergreen_reference_2009.txt`

**Evidence:**
> Ability to select Run ASAP, Hourly, Daily, Weekly, Monthly, Yearly

### REQ-077: Report output formats (Excel, HTML, CSV)

Reports shall be exportable or viewable in Excel, HTML, and CSV formats to support both web viewing and spreadsheet/data export use cases.

**Priority:** MUST

**Traceability:**
- `early_draft_srs_galecia.txt`
- `meeting_tech_subcommittee_2009-06-30.txt`

**Evidence:**
> Output would be in Excel, HTML, and CSV format
> Excel, HTML, and CSV formats are required.

### REQ-078: Email report delivery with address book

The system should send report results to specified email addresses and support an address book of frequently used email addresses to support recurring and administrative reporting.

**Priority:** SHOULD

**Traceability:**
- `early_draft_srs_galecia.txt`
- `evergreen_reference_2009.txt`

**Evidence:**
> Ability to enter email addresses for report to be sent to - would be great to have an address book
> No email delivery ... reports can only be downloaded

### REQ-079: Pivot table output

The reporting system should provide pivot-table output to enable directors and business users to analyze report results using pivot views.

**Priority:** SHOULD

**Traceability:**
- `early_draft_srs_galecia.txt`
- `survey_results_2009.txt`

**Evidence:**
> Pivot table output
> Pivot table output would be great

### REQ-080: Include null and blank fields in report results

Reports shall include null and blank fields regardless of the selected filters or selected display fields so that omission does not mislead users.

**Priority:** MUST

**Traceability:**
- `early_draft_srs_galecia.txt`
- `meeting_tech_subcommittee_2009-06-30.txt`

**Evidence:**
> All nulls and blank fields must be included in the results no matter what is being filtered or displayed

### REQ-081: Real-time reporting against current data

The system should support real-time reporting against current data for reports that require up-to-the-moment operational status (for example, what is overdue today).

**Priority:** SHOULD

**Traceability:**
- `early_draft_srs_galecia.txt`
- `meeting_tech_subcommittee_2009-06-30.txt`

**Evidence:**
> Ability to have real time reporting
> Some reports need to be real-time - like 'what's overdue today,'

### REQ-082: Historical reporting snapshots for specified dates or date ranges

The system shall support historical reporting for a specified date or date range, including historical snapshots, so users can see what the data looked like in the past even after changes.

**Priority:** SHOULD

**Traceability:**
- `early_draft_srs_galecia.txt`
- `survey_results_2009.txt`

**Evidence:**
> Ability to have historical reporting - a reporting warehouse such that data can be acquired on a given date or range
> Historical reporting - I want to see what the data looked like on a specific date in the past

### REQ-083: Transaction history retention with configurable window and indefinite aggregates

The system shall retain transaction history for a configurable period and retain monthly and annual aggregates indefinitely to support privacy/compliance and long-term statistics.

**Priority:** MUST

**Traceability:**
- `early_draft_srs_galecia.txt`
- `survey_results_2009.txt`

**Evidence:**
> Transaction history is maintained for X days (X is configurable). Monthly and annual aggregate information is maintained indefinitely.

### REQ-084: Privacy-preserving transaction archive with anonymization

The system shall archive transaction data while protecting personally identifiable patron information according to applicable law, and the data used to produce useful demographic statistics shall be anonymized.

**Priority:** MUST

**Traceability:**
- `email_report_features.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> Transactions archived protecting patron privacy per State Law, while providing useful demographic statistics.
> The data used to produce these statistics must be anonymized

### REQ-085: Transaction grouping dimensions

The system shall group transaction data by hour, terminal, branch, and system to support operational and productivity analysis.

**Priority:** MUST

**Traceability:**
- `survey_results_2009.txt`
- `early_draft_srs_galecia.txt`

**Evidence:**
> Transactions can be grouped by hour, terminal, branch, and system.

### REQ-086: Check-in type counts

The system shall count check-ins individually and cumulatively by book drop, terminal, user, and self-service so that check-in methods are distinguishable in reports.

**Priority:** MUST

**Traceability:**
- `survey_results_2009.txt`
- `early_draft_srs_galecia.txt`

**Evidence:**
> All types of check-in counted individually and cumulatively: book-drop, terminal, by user or self-service.

### REQ-087: Check-out type counts

The system shall count check-outs individually and cumulatively by staff checkout, self-checkout, staff renewal, self-checkout renewal, online renewal, and OPAC renewal to support circulation distinctions in reports.

**Priority:** MUST

**Traceability:**
- `survey_results_2009.txt`
- `early_draft_srs_galecia.txt`

**Evidence:**
> All types of check-out counted individually and cumulatively: staff checkout, self checkout, staff renewal, self checkout renewal, online renewal, OPAC renewal.

### REQ-088: Hold placement method counts

The system shall count holds by placement method, including staff desk, public computer, and remote placement.

**Priority:** MUST

**Traceability:**
- `survey_results_2009.txt`
- `early_draft_srs_galecia.txt`

**Evidence:**
> Holds counted with method of placement: at staff desk, public computer, or remotely.

### REQ-089: Transactions report scope by patron and organizational levels

The transactions report shall report holds placed, holds filled, and checkouts by patron, by library, by a selected group of libraries, by system, and by county so users can analyze transactions across multiple scopes.

**Priority:** MUST

**Traceability:**
- `survey_results_2009.txt`
- `early_draft_srs_galecia.txt`

**Evidence:**
> The system can generate a report of transactions ... per patron, per library, per selected group of libraries, per system, per county.

### REQ-090: Anonymized demographic statistics by geography and age range

The system shall provide anonymized demographic statistics by geography and age range to allow analysis without exposing patron identities.

**Priority:** MUST

**Traceability:**
- `survey_results_2009.txt`
- `early_draft_srs_galecia.txt`

**Evidence:**
> Demographic statistics include transactions by geographical regions and age ranges. Data must be anonymized.

### REQ-091: Patron behavior analysis statistics (predictive/behavior measures)

The system should produce statistics describing or predicting patron behavior and material use, including return speed, renewal likelihood, and renewal percentages to support service and collection planning.

**Priority:** SHOULD

**Traceability:**
- `survey_results_2009.txt`
- `early_draft_srs_galecia.txt`

**Evidence:**
> The system should produce statistics that can be used to understand and predict patron behavior and use of materials.
> How likely is a particular book to be renewed?

### REQ-092: Value of items reporting by portion or entire collection

The system shall report the value of all items or a selected portion based on item-record value data, including support for examples such as long-overdue items or the entire collection.

**Priority:** MUST

**Traceability:**
- `email_financial_reports.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> System can generate a report of the value of items ... in the entire collection or a portion.
> Value of all items with status of "longoverdue"

### REQ-093: Patron account balance reporting

The system shall report patron account balances by patron, home library, and system.

**Priority:** MUST

**Traceability:**
- `email_financial_reports.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> Patron account balances by patron, home library, and system

### REQ-094: Fines and charges reporting by time period and charge type

The system shall report fines and charges accrued per time period and per charge type, where time period and types include items described such as last twelve months, year-to-date, last month, and charge types such as overdue, damaged, and lost-item charges.

**Priority:** MUST

**Traceability:**
- `email_financial_reports.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> Fines and charges accrued per time period ... and per type of charge
> Fines and charges accrued per time period ... and per type of charge

### REQ-095: Fines waived reporting by time period and branch

The system shall report fines waived by time period and branch so that waived fines can be tracked against each library’s budget.

**Priority:** MUST

**Traceability:**
- `email_financial_reports.eml`

**Evidence:**
> Fines waived per time period and per branch
> Fines waived should be tracked per library

### REQ-096: Payments reporting by time period, library, and payment method

The system shall report payments by time period, library, and payment method, including methods such as staff desk, self-check, OPAC, cash, credit card, and check.

**Priority:** MUST

**Traceability:**
- `email_financial_reports.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> Payments made per time period and per payment method
> The financial reports need to show payments by method - cash, credit card, check, etc.

### REQ-097: Financial payment ledger linking payments to charges

The system shall maintain a ledger linking each patron payment to the specific charge to which it was applied so payments can be traced back for reconciliation and auditability.

**Priority:** MUST

**Traceability:**
- `email_financial_reports.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> The system maintains a ledger of patron payments, including which charges payments are applied to
> They need to be able to trace every payment back to the specific charge

### REQ-098: Financial balance query by minimum amount

Staff shall be able to query patron accounts with balances greater than a specified dollar amount to identify accounts requiring attention.

**Priority:** SHOULD

**Traceability:**
- `email_financial_reports.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> A staff user can easily query patron accounts with balances greater than X dollars.

### REQ-099: Immediate reflection of front-desk financial updates

Financial information shall be easily updatable and reflect front-desk payments immediately so reports and balances stay current.

**Priority:** SHOULD

**Traceability:**
- `email_financial_reports.eml`

**Evidence:**
> Financial information needs to be easily updatable.
> the system to reflect that immediately

### REQ-100: Financial compliance with accounting and audit requirements

Reports and data archiving shall comply with standard accounting practices and state, county, and municipal auditing requirements.

**Priority:** MUST

**Traceability:**
- `email_financial_reports.eml`
- `early_draft_srs_galecia.txt`

**Evidence:**
> All reports and data archiving must comply with standard accounting practice and state, county, and municipal auditing requirements.

### REQ-101: Enforce financial data retention policies

The system shall enforce applicable financial data retention policies, including multi-year retention periods where required (for example, seven years for audit purposes).

**Priority:** MUST

**Traceability:**
- `email_financial_reports.eml`

**Evidence:**
> The system needs to enforce retention policies.
> Some data needs to be retained for 7 years for audit purposes.

### REQ-102: Consortium operating scale support

The system shall support a consortium with 286 locations, approximately 17 million annual circulations, and over 900,000 items purchased or processed annually.

**Priority:** MUST

**Traceability:**
- `early_draft_srs_galecia.txt`
- `meeting_minutes/meeting_2009-07-20_minutes.txt`

**Evidence:**
> The system must support a library consortium with 286 locations, 17 million annual circulations, and purchasing/processing over 900,000 items per year.

### REQ-103: Report and search processing during open hours without disruption

Searches and reports shall be processable during open hours without disrupting other system functions, including circulation operations.

**Priority:** MUST

**Traceability:**
- `interview_sysadmin_2009-05-10.txt`
- `meeting_minutes/meeting_2009-07-20_minutes.txt`

**Evidence:**
> The key requirement is that searches and reports can be processed during open hours without disrupting other system functions.

### REQ-104: Supported server environments

The system shall operate on Linux and Solaris server environments to match deployment needs.

**Priority:** MUST

**Traceability:**
- `early_draft_srs_galecia.txt`
- `interview_sysadmin_2009-05-10.txt`

**Evidence:**
> The system must operate on a Linux or Solaris server environment.
> any reporting system needs to work on both Linux and Solaris.

### REQ-105: Client access via web browser or Windows-compatible client

The system shall be accessible through a web browser or a Windows-compatible client so different library setups can use it.

**Priority:** MUST

**Traceability:**
- `early_draft_srs_galecia.txt`
- `meeting_minutes/meeting_2009-07-20_minutes.txt`

**Evidence:**
> The system must be accessible through a web browser or a Windows-compatible client.

### REQ-106: Legacy web browser support

If web-based, the system shall support Microsoft Internet Explorer 6.0 or later and Mozilla Firefox 2.0 or later.

**Priority:** MUST

**Traceability:**
- `early_draft_srs_galecia.txt`
- `interview_sysadmin_2009-05-10.txt`

**Evidence:**
> The system must be accessible through Microsoft Internet Explorer (version 6.0 and later) and Mozilla Firefox (version 2.0 and later).

### REQ-107: Accessibility support including Section 508

The system shall be usable with screen readers, screen magnification software, and other assistive technologies, and it shall comply with Section 508 accessibility requirements.

**Priority:** MUST

**Traceability:**
- `early_draft_srs_galecia.txt`
- `interview_sysadmin_2009-05-10.txt`

**Evidence:**
> The system must be accessible with screen-reading software, screen-magnification software, and other assistive technology programs
> This is non-negotiable ... MUST comply with Section 508 accessibility requirements.

### REQ-108: Standards-compliant HTML output

Web interfaces, help content, and report output shall produce standards-compliant HTML and validate against W3C standards to support compatibility and accessibility.

**Priority:** MUST

**Traceability:**
- `early_draft_srs_galecia.txt`
- `meeting_tech_subcommittee_2009-06-30.txt`

**Evidence:**
> The system must produce standards-compliant HTML output for web-based components.
> All HTML output validates against W3C standards

### REQ-109: Relational database backend

The system shall use a fully relational database backend so the reporting layer works with relational data structures.

**Priority:** MUST

**Traceability:**
- `early_draft_srs_galecia.txt`
- `meeting_tech_subcommittee_2009-06-30.txt`

**Evidence:**
> The system must use a fully relational database back-end.
> The system must use a fully relational database back-end.

### REQ-110: Separate development, training, and production environments

The system shall provide separate development, training, and production environments so staff can test and practice without affecting production data.

**Priority:** MUST

**Traceability:**
- `interview_sysadmin_2009-05-10.txt`
- `meeting_tech_subcommittee_2009-06-30.txt`

**Evidence:**
> We definitely need separate environments.
> The training environment needs to be safe - staff should be able to experiment without risking production data.

### REQ-111: Configuration migration between environments via export/import

The system shall support exporting and importing report templates, permission settings, saved queries, and other configurations between environments so configurations created in development/training can be migrated to production.

**Priority:** MUST

**Traceability:**
- `interview_sysadmin_2009-05-10.txt`
- `meeting_tech_subcommittee_2009-06-30.txt`

**Evidence:**
> configurations developed in training/dev need to be migratable to production.
> Export/import of templates, permission settings, and saved queries.

### REQ-112: OPAC isolation from management reporting

Management reporting shall not constrain or slow down OPAC functionality, and if a report is running it should not degrade OPAC operation.

**Priority:** MUST

**Traceability:**
- `interview_sysadmin_2009-05-10.txt`
- `meeting_tech_subcommittee_2009-06-30.txt`

**Evidence:**
> The management reporting system must not constrain the OPAC in any way.
> If a report is running, it should not slow down the OPAC.

### REQ-113: Online hierarchical cross-linked searchable help system

The system shall provide an online, hierarchical, cross-linked, searchable HTML help system describing all functions for staff self-service guidance.

**Priority:** MUST

**Traceability:**
- `early_draft_srs_galecia.txt`
- `interview_sysadmin_2009-05-10.txt`

**Evidence:**
> The system must provide an online, hierarchical, and cross-linked help system in HTML
> The HTML help needs to be searchable and easy to navigate.

### REQ-114: Error reporting with high-level and query-specific diagnostics

The system shall provide meaningful high-level errors and query-specific diagnostic feedback to administrators, including specifics sufficient to diagnose failures (e.g., which table/field and what kind of error).

**Priority:** SHOULD

**Traceability:**
- `early_draft_srs_galecia.txt`
- `meeting_tech_subcommittee_2009-06-30.txt`

**Evidence:**
> The system must provide thorough high-level error reporting and feedback
> We need specifics - which table, which field, what kind of error.

### REQ-115: Developer-provided complete data specifications for management processes

The developer shall provide complete data specifications (data dictionaries) for authority, bibliographic, order, item, hold/request, and other records accessed by management/reporting processes.

**Priority:** SHOULD

**Traceability:**
- `early_draft_srs_galecia.txt`
- `meeting_tech_subcommittee_2009-06-30.txt`

**Evidence:**
> The developer must provide complete data specifications for authority records, bibliographic records, order records, item records, hold/request records, and other records

### REQ-116: Developer documentation of major management processes

The developer shall document major processes, including bibliographic import/export, authority validation, and standard reports, so staff can understand how reportable data is produced and managed.

**Priority:** SHOULD

**Traceability:**
- `early_draft_srs_galecia.txt`
- `meeting_tech_subcommittee_2009-06-30.txt`

**Evidence:**
> The developer must provide a thorough high-level description of major processes

## Discarded Requirements

### Discarded candidate

**Original statement:** The system shall report the volume of material in a specified library at any point in time.

**Reason:** Merged into REQ-001; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines014_material_volume.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The material volume report shall separately count new acquisitions, checked-in items, and checked-out items, and provide a total.

**Reason:** Merged into REQ-002; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines014_material_volume.eml`

### Discarded candidate

**Original statement:** The material volume report shall support category breakdowns including total items, holds, adult fiction, and board books.

**Reason:** Merged into REQ-003; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines014_material_volume.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** Users shall be able to customize the categories used in material volume reports.

**Reason:** Merged into REQ-004; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines014_material_volume.eml`

### Discarded candidate

**Original statement:** The system shall support date filters for reporting material volume at historical points in time.

**Reason:** Merged into REQ-005; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines014_material_volume.eml`

### Discarded candidate

**Original statement:** The system shall provide an interface showing the capacity of all branches at once.

**Reason:** Merged into REQ-006; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines015_capacity_interface.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The capacity interface shall provide a high-level summary view containing all branches and key metrics.

**Reason:** Merged into REQ-006; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines015_capacity_interface.eml`

### Discarded candidate

**Original statement:** The capacity interface shall allow users to drill down into individual branches.

**Reason:** Merged into REQ-007; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines015_capacity_interface.eml`

### Discarded candidate

**Original statement:** The capacity interface shall support sorting and filtering by region, library type, and current load.

**Reason:** Merged into REQ-008; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines015_capacity_interface.eml`

### Discarded candidate

**Original statement:** The capacity interface shall display branch growth or shrinkage trends.

**Reason:** Merged into REQ-009; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines015_capacity_interface.eml`

### Discarded candidate

**Original statement:** The capacity interface shall allow users to export results to CSV.

**Reason:** Merged into REQ-010; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines015_capacity_interface.eml`

### Discarded candidate

**Original statement:** The system shall compare, for each genre and format, the percentage of total circulations, percentage of the collection, and percentage of total shelf space.

**Reason:** Merged into REQ-011; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines016_shelf_space.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The shelf space report shall be available at both library and system levels.

**Reason:** Merged into REQ-012; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines016_shelf_space.eml`

### Discarded candidate

**Original statement:** The shelf space report should support filtering by date range.

**Reason:** Merged into REQ-013; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines016_shelf_space.eml`

### Discarded candidate

**Original statement:** The system should provide a side-by-side comparison view of library breakdowns.

**Reason:** Merged into REQ-014; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines016_shelf_space.eml`

### Discarded candidate

**Original statement:** The system shall estimate shelf space by item dimensions or use item count as a proxy when direct shelf-space data is unavailable.

**Reason:** Merged into REQ-015; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines016_shelf_space.eml`

### Discarded candidate

**Original statement:** The system shall provide a utility for transferring batches of items between branches.

**Reason:** Merged into REQ-016; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines018_item_transfer.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The transfer utility shall allow users to query for candidate materials.

**Reason:** Merged into REQ-017; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines018_item_transfer.eml`

### Discarded candidate

**Original statement:** The transfer utility shall allow users to save and reuse candidate-selection queries.

**Reason:** Merged into REQ-018; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines018_item_transfer.eml`

### Discarded candidate

**Original statement:** The transfer utility shall allow users to manually select individual titles or items from query results.

**Reason:** Merged into REQ-019; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines018_item_transfer.eml`

### Discarded candidate

**Original statement:** The transfer utility shall change the location records of selected items to a new location.

**Reason:** Merged into REQ-020; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines018_item_transfer.eml`

### Discarded candidate

**Original statement:** The transfer utility shall generate printable pull lists for selected items.

**Reason:** Merged into REQ-021; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines018_item_transfer.eml`

### Discarded candidate

**Original statement:** The transfer utility shall show a preview of proposed changes and require confirmation before applying them.

**Reason:** Merged into REQ-022; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines018_item_transfer.eml`

### Discarded candidate

**Original statement:** The transfer utility shall provide an undo function for transfers.

**Reason:** Merged into REQ-023; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines018_item_transfer.eml`

### Discarded candidate

**Original statement:** The system shall restrict item transfers to authorized roles such as managers, administrators, or transfer coordinators.

**Reason:** Merged into REQ-024; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines018_item_transfer.eml`

### Discarded candidate

**Original statement:** The system shall track transfer history for each item.

**Reason:** Merged into REQ-025; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines018_item_transfer.eml`

### Discarded candidate

**Original statement:** The system shall revert transferred items to their original location after a configured period or when configured criteria are met.

**Reason:** Merged into REQ-026; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines018_item_transfer.eml`

### Discarded candidate

**Original statement:** The system should support event-based transfer reversion, including item status changes and checkout at the destination.

**Reason:** Merged into REQ-027; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines018_item_transfer.eml`

### Discarded candidate

**Original statement:** The transfer utility should generate printable transit labels or barcodes for transferred items.

**Reason:** Merged into REQ-028; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines018_item_transfer.eml`

### Discarded candidate

**Original statement:** The system should notify users when a transfer is delayed or has issues.

**Reason:** Merged into REQ-029; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines018_item_transfer.eml`

### Discarded candidate

**Original statement:** The system shall log all transfers for audit purposes.

**Reason:** Merged into REQ-030; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines018_item_transfer.eml`

### Discarded candidate

**Original statement:** The system shall provide reports of missing and damaged items per branch.

**Reason:** Merged into REQ-031; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines019_020_missing_intransit.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The missing and damaged items report should include item condition notes.

**Reason:** Merged into REQ-032; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines019_020_missing_intransit.eml`

### Discarded candidate

**Original statement:** The missing and damaged items report should support date-range filtering.

**Reason:** Merged into REQ-033; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines019_020_missing_intransit.eml`

### Discarded candidate

**Original statement:** The system shall list items that have been in transit longer than a configurable number of days, per branch and per system.

**Reason:** Merged into REQ-034; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines019_020_missing_intransit.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The in-transit report shall merge transit-to and transit-from items into one report.

**Reason:** Merged into REQ-035; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines019_020_missing_intransit.eml`

### Discarded candidate

**Original statement:** The in-transit report should support sorting by due date.

**Reason:** Merged into REQ-036; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines019_020_missing_intransit.eml`

### Discarded candidate

**Original statement:** The system shall identify item records for purging using customizable criteria.

**Reason:** Merged into REQ-037; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines021_item_purging.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The purging utility shall allow status-based, time-based, and activity-based criteria to be combined with logical conditions.

**Reason:** Merged into REQ-038; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines021_item_purging.eml`

### Discarded candidate

**Original statement:** The system shall provide a report and utility for converting many items from one status to another in batch.

**Reason:** Merged into REQ-039; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines021_item_purging.eml`

### Discarded candidate

**Original statement:** The system shall provide a last-copy report identifying the last copy within a selected library or entire system.

**Reason:** Merged into REQ-040; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines021_item_purging.eml`
- `interview_cataloging_2009-05-08.txt`

### Discarded candidate

**Original statement:** The system shall provide a quick method to delete volume entries together with copy entries and to delete records with no attached items.

**Reason:** Merged into REQ-041; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines021_item_purging.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The system shall show purge candidates in read-only reports and require a separate confirmation step before deletion.

**Reason:** Merged into REQ-042; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines021_item_purging.eml`

### Discarded candidate

**Original statement:** The system shall maintain an audit trail of all purges, including who purged what and when.

**Reason:** Merged into REQ-043; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines021_item_purging.eml`

### Discarded candidate

**Original statement:** The system shall count and track deletions of records such as item and patron records by location and system.

**Reason:** Merged into REQ-044; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines022_deletions.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** Deletion records shall include record type, record identifier, timestamp, deleting user, and user location.

**Reason:** Merged into REQ-045; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines022_deletions.eml`

### Discarded candidate

**Original statement:** The deletion report shall support aggregation by date range, user, record type, location, and system.

**Reason:** Merged into REQ-046; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines022_deletions.eml`

### Discarded candidate

**Original statement:** The system should track deletion attempts that were denied.

**Reason:** Merged into REQ-047; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines022_deletions.eml`

### Discarded candidate

**Original statement:** The system shall allow reports to be filtered and grouped by age range, zip code, county, home branch, patron type, and preferred language.

**Reason:** Merged into REQ-048; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines023_patron_characteristics.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** Patron reports shall support configurable age brackets per report.

**Reason:** Merged into REQ-049; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines023_patron_characteristics.eml`

### Discarded candidate

**Original statement:** Patron reports shall support combining demographic filters with AND and OR logic.

**Reason:** Merged into REQ-050; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines023_patron_characteristics.eml`

### Discarded candidate

**Original statement:** Patron reports shall include patrons with null or missing optional demographic values.

**Reason:** Merged into REQ-051; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines023_patron_characteristics.eml`

### Discarded candidate

**Original statement:** The system shall generate a list of patrons with no circulation or electronic activity during a configurable number of preceding days.

**Reason:** Merged into REQ-052; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines024_inactive_patrons.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The inactive patron report shall support system, home library, county, and other configured aggregation levels.

**Reason:** Merged into REQ-053; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines024_inactive_patrons.eml`

### Discarded candidate

**Original statement:** Electronic activity for inactive-patron reporting shall include OPAC or patron-account logins, online hold placement, online renewals, and logged digital-resource access.

**Reason:** Merged into REQ-054; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines024_inactive_patrons.eml`

### Discarded candidate

**Original statement:** The inactive patron report shall identify patrons with outstanding fines separately.

**Reason:** Merged into REQ-055; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines024_inactive_patrons.eml`

### Discarded candidate

**Original statement:** The inactive patron report shall allow exclusion of patrons based on flags or types, including do-not-disturb, VIP, staff, and communication opt-out.

**Reason:** Merged into REQ-056; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines024_inactive_patrons.eml`

### Discarded candidate

**Original statement:** The inactive patron report shall include current mailing addresses.

**Reason:** Merged into REQ-057; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines024_inactive_patrons.eml`

### Discarded candidate

**Original statement:** The inactive patron report shall be exportable in CSV format.

**Reason:** Merged into REQ-058; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines024_inactive_patrons.eml`

### Discarded candidate

**Original statement:** Long-running reports shall execute in the background and cache results where necessary.

**Reason:** Merged into REQ-059; duplicate concept was already captured there.

**Sources:**
- `conversations/conv_pines024_inactive_patrons.eml`
- `interview_sysadmin_2009-05-10.txt`

### Discarded candidate

**Original statement:** The system shall provide a user-friendly query interface for bibliographic, item, patron, transaction, and financial records.

**Reason:** Merged into REQ-060; duplicate concept was already captured there.

**Sources:**
- `email_report_features.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The query tool shall allow users to select fields, choose values from picklists, use regular expressions, and apply Boolean operators.

**Reason:** Merged into REQ-061; duplicate concept was already captured there.

**Sources:**
- `email_report_features.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** Administrators shall be able to create report templates that staff can run as-is or modify within administrator-defined limits.

**Reason:** Merged into REQ-062; duplicate concept was already captured there.

**Sources:**
- `email_report_features.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** Authorized users shall be able to clone existing report templates into new variants.

**Reason:** Merged into REQ-063; duplicate concept was already captured there.

**Sources:**
- `email_report_features.eml`

### Discarded candidate

**Original statement:** The system shall provide fine-grained permissions controlling who can create, clone, run, and modify reports.

**Reason:** Merged into REQ-064; duplicate concept was already captured there.

**Sources:**
- `email_report_features.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** Administrators shall be able to create shared folders that allow or disallow staff from running specified reports.

**Reason:** Merged into REQ-065; duplicate concept was already captured there.

**Sources:**
- `email_report_features.eml`

### Discarded candidate

**Original statement:** User rights and privileges shall be controlled through security groups or roles assignable to individuals, workgroups, and arbitrary staff groups.

**Reason:** Merged into REQ-066; duplicate concept was already captured there.

**Sources:**
- `email_staff_login.eml`
- `interview_sysadmin_2009-05-10.txt`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The system shall support optional streamlined staff login methods such as card or RFID badge swipe.

**Reason:** Merged into REQ-067; duplicate concept was already captured there.

**Sources:**
- `email_staff_login.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The system shall support individual username-and-password staff login as an alternative to streamlined login.

**Reason:** Merged into REQ-068; duplicate concept was already captured there.

**Sources:**
- `email_staff_login.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The system shall identify the individual staff member authenticated through any login method for audit purposes.

**Reason:** Merged into REQ-069; duplicate concept was already captured there.

**Sources:**
- `email_staff_login.eml`

### Discarded candidate

**Original statement:** The system shall provide predefined board and executive reports containing circulation, check-in, holds, and usage statistics.

**Reason:** Merged into REQ-070; duplicate concept was already captured there.

**Sources:**
- `email_report_features.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** Activity reports shall support cross-tabulation by terminal, branch, system, hour, patron age range, patron type, and patron location.

**Reason:** Merged into REQ-071; duplicate concept was already captured there.

**Sources:**
- `email_report_features.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** Report results shall display the query selections and criteria used to generate them.

**Reason:** Merged into REQ-072; duplicate concept was already captured there.

**Sources:**
- `email_report_features.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** Users shall be able to see a submitted report's queue position, number of reports ahead, submission time, and status.

**Reason:** Merged into REQ-073; duplicate concept was already captured there.

**Sources:**
- `email_report_features.eml`
- `evergreen_reference_2009.txt`

### Discarded candidate

**Original statement:** Authorized users shall be able to prioritize important reports in the report queue.

**Reason:** Merged into REQ-074; duplicate concept was already captured there.

**Sources:**
- `email_report_features.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** Users shall be able to cancel scheduled or currently running reports.

**Reason:** Merged into REQ-075; duplicate concept was already captured there.

**Sources:**
- `early_draft_srs_galecia.txt`
- `meeting_tech_subcommittee_2009-06-30.txt`

### Discarded candidate

**Original statement:** The system shall support ASAP, hourly, daily, weekly, monthly, and yearly report scheduling.

**Reason:** Merged into REQ-076; duplicate concept was already captured there.

**Sources:**
- `early_draft_srs_galecia.txt`
- `evergreen_reference_2009.txt`

### Discarded candidate

**Original statement:** Reports shall be exportable or viewable in Excel, HTML, and CSV formats.

**Reason:** Merged into REQ-077; duplicate concept was already captured there.

**Sources:**
- `early_draft_srs_galecia.txt`
- `meeting_tech_subcommittee_2009-06-30.txt`

### Discarded candidate

**Original statement:** The system should send report results to specified email addresses and support an address book of frequently used addresses.

**Reason:** Merged into REQ-078; duplicate concept was already captured there.

**Sources:**
- `early_draft_srs_galecia.txt`
- `evergreen_reference_2009.txt`

### Discarded candidate

**Original statement:** The reporting system should provide pivot-table output.

**Reason:** Merged into REQ-079; duplicate concept was already captured there.

**Sources:**
- `early_draft_srs_galecia.txt`
- `survey_results_2009.txt`

### Discarded candidate

**Original statement:** Reports shall include null and blank fields regardless of the selected filters or display fields.

**Reason:** Merged into REQ-080; duplicate concept was already captured there.

**Sources:**
- `early_draft_srs_galecia.txt`
- `meeting_tech_subcommittee_2009-06-30.txt`

### Discarded candidate

**Original statement:** The system should support real-time reporting against current data.

**Reason:** Merged into REQ-081; duplicate concept was already captured there.

**Sources:**
- `early_draft_srs_galecia.txt`
- `meeting_tech_subcommittee_2009-06-30.txt`

### Discarded candidate

**Original statement:** The system shall support historical reporting for a specified date or date range, including historical snapshots.

**Reason:** Merged into REQ-082; duplicate concept was already captured there.

**Sources:**
- `early_draft_srs_galecia.txt`
- `survey_results_2009.txt`

### Discarded candidate

**Original statement:** The system shall retain transaction history for a configurable period and retain monthly and annual aggregates indefinitely.

**Reason:** Merged into REQ-083; duplicate concept was already captured there.

**Sources:**
- `early_draft_srs_galecia.txt`
- `survey_results_2009.txt`

### Discarded candidate

**Original statement:** The system shall archive transaction data while protecting personally identifiable patron information in accordance with applicable law.

**Reason:** Merged into REQ-084; duplicate concept was already captured there.

**Sources:**
- `email_report_features.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The system shall group transaction data by hour, terminal, branch, and system.

**Reason:** Merged into REQ-085; duplicate concept was already captured there.

**Sources:**
- `survey_results_2009.txt`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The system shall count check-ins individually and cumulatively by book drop, terminal, user, and self-service.

**Reason:** Merged into REQ-086; duplicate concept was already captured there.

**Sources:**
- `survey_results_2009.txt`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The system shall count check-outs individually and cumulatively by staff checkout, self-checkout, staff renewal, self-checkout renewal, online renewal, and OPAC renewal.

**Reason:** Merged into REQ-087; duplicate concept was already captured there.

**Sources:**
- `survey_results_2009.txt`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The system shall count holds by placement method, including staff desk, public computer, and remote placement.

**Reason:** Merged into REQ-088; duplicate concept was already captured there.

**Sources:**
- `survey_results_2009.txt`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The transactions report shall report holds placed, holds filled, and checkouts by patron, library, selected library group, system, and county.

**Reason:** Merged into REQ-089; duplicate concept was already captured there.

**Sources:**
- `survey_results_2009.txt`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The system shall provide anonymized demographic statistics by geography and age range.

**Reason:** Merged into REQ-090; duplicate concept was already captured there.

**Sources:**
- `survey_results_2009.txt`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The system should produce statistics describing or predicting patron behavior and material use, including return speed, renewal likelihood, and renewal percentages.

**Reason:** Merged into REQ-091; duplicate concept was already captured there.

**Sources:**
- `survey_results_2009.txt`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The system shall report the value of all items or a selected portion based on item-record value data.

**Reason:** Merged into REQ-092; duplicate concept was already captured there.

**Sources:**
- `email_financial_reports.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The system shall report patron account balances by patron, home library, and system.

**Reason:** Merged into REQ-093; duplicate concept was already captured there.

**Sources:**
- `email_financial_reports.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The system shall report fines and charges by time period and charge type.

**Reason:** Merged into REQ-094; duplicate concept was already captured there.

**Sources:**
- `email_financial_reports.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The system shall report fines waived by time period and branch.

**Reason:** Merged into REQ-095; duplicate concept was already captured there.

**Sources:**
- `email_financial_reports.eml`

### Discarded candidate

**Original statement:** The system shall report payments by time period, library, and payment method.

**Reason:** Merged into REQ-096; duplicate concept was already captured there.

**Sources:**
- `email_financial_reports.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The system shall maintain a ledger linking each patron payment to the specific charge to which it was applied.

**Reason:** Merged into REQ-097; duplicate concept was already captured there.

**Sources:**
- `email_financial_reports.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** Staff shall be able to query patron accounts with balances greater than a specified dollar amount.

**Reason:** Merged into REQ-098; duplicate concept was already captured there.

**Sources:**
- `email_financial_reports.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** Financial information shall be easily updatable and reflect front-desk payments immediately.

**Reason:** Merged into REQ-099; duplicate concept was already captured there.

**Sources:**
- `email_financial_reports.eml`

### Discarded candidate

**Original statement:** Reports and data archiving shall comply with standard accounting practices and state, county, and municipal auditing requirements.

**Reason:** Merged into REQ-100; duplicate concept was already captured there.

**Sources:**
- `email_financial_reports.eml`
- `early_draft_srs_galecia.txt`

### Discarded candidate

**Original statement:** The system shall enforce applicable financial data retention policies, including required multi-year retention periods.

**Reason:** Merged into REQ-101; duplicate concept was already captured there.

**Sources:**
- `email_financial_reports.eml`

### Discarded candidate

**Original statement:** The system shall support a consortium with 286 locations, approximately 17 million annual circulations, and more than 900,000 items purchased or processed annually.

**Reason:** Merged into REQ-102; duplicate concept was already captured there.

**Sources:**
- `early_draft_srs_galecia.txt`
- `meeting_minutes/meeting_2009-07-20_minutes.txt`

### Discarded candidate

**Original statement:** Searches and reports shall be processable during open hours without disrupting other system functions.

**Reason:** Merged into REQ-103; duplicate concept was already captured there.

**Sources:**
- `interview_sysadmin_2009-05-10.txt`
- `meeting_minutes/meeting_2009-07-20_minutes.txt`

### Discarded candidate

**Original statement:** The system shall operate on Linux and Solaris server environments.

**Reason:** Merged into REQ-104; duplicate concept was already captured there.

**Sources:**
- `early_draft_srs_galecia.txt`
- `interview_sysadmin_2009-05-10.txt`

### Discarded candidate

**Original statement:** The system shall be accessible through a web browser or a Windows-compatible client.

**Reason:** Merged into REQ-105; duplicate concept was already captured there.

**Sources:**
- `early_draft_srs_galecia.txt`
- `meeting_minutes/meeting_2009-07-20_minutes.txt`

### Discarded candidate

**Original statement:** If web-based, the system shall support Microsoft Internet Explorer 6.0 or later and Mozilla Firefox 2.0 or later.

**Reason:** Merged into REQ-106; duplicate concept was already captured there.

**Sources:**
- `early_draft_srs_galecia.txt`
- `interview_sysadmin_2009-05-10.txt`

### Discarded candidate

**Original statement:** The system shall be usable with screen readers, screen magnification software, and other assistive technologies, including support for Section 508 accessibility.

**Reason:** Merged into REQ-107; duplicate concept was already captured there.

**Sources:**
- `early_draft_srs_galecia.txt`
- `interview_sysadmin_2009-05-10.txt`

### Discarded candidate

**Original statement:** Web interfaces, help content, and report output shall produce standards-compliant HTML.

**Reason:** Merged into REQ-108; duplicate concept was already captured there.

**Sources:**
- `early_draft_srs_galecia.txt`
- `meeting_tech_subcommittee_2009-06-30.txt`

### Discarded candidate

**Original statement:** The system shall use a fully relational database backend.

**Reason:** Merged into REQ-109; duplicate concept was already captured there.

**Sources:**
- `early_draft_srs_galecia.txt`
- `meeting_tech_subcommittee_2009-06-30.txt`

### Discarded candidate

**Original statement:** The system shall provide separate development, training, and production environments.

**Reason:** Merged into REQ-110; duplicate concept was already captured there.

**Sources:**
- `interview_sysadmin_2009-05-10.txt`
- `meeting_tech_subcommittee_2009-06-30.txt`

### Discarded candidate

**Original statement:** The system shall support exporting and importing report templates, permission settings, saved queries, and other configurations between environments.

**Reason:** Merged into REQ-111; duplicate concept was already captured there.

**Sources:**
- `interview_sysadmin_2009-05-10.txt`
- `meeting_tech_subcommittee_2009-06-30.txt`

### Discarded candidate

**Original statement:** Management reporting shall not constrain or slow down OPAC functionality.

**Reason:** Merged into REQ-112; duplicate concept was already captured there.

**Sources:**
- `interview_sysadmin_2009-05-10.txt`
- `meeting_tech_subcommittee_2009-06-30.txt`

### Discarded candidate

**Original statement:** The system shall provide an online, hierarchical, cross-linked, searchable HTML help system describing all functions.

**Reason:** Merged into REQ-113; duplicate concept was already captured there.

**Sources:**
- `early_draft_srs_galecia.txt`
- `interview_sysadmin_2009-05-10.txt`

### Discarded candidate

**Original statement:** The system shall provide meaningful high-level errors and query-specific diagnostic feedback to administrators.

**Reason:** Merged into REQ-114; duplicate concept was already captured there.

**Sources:**
- `early_draft_srs_galecia.txt`
- `meeting_tech_subcommittee_2009-06-30.txt`

### Discarded candidate

**Original statement:** The developer shall provide complete data specifications for authority, bibliographic, order, item, hold/request, and other records accessed by management processes.

**Reason:** Merged into REQ-115; duplicate concept was already captured there.

**Sources:**
- `early_draft_srs_galecia.txt`
- `meeting_tech_subcommittee_2009-06-30.txt`

### Discarded candidate

**Original statement:** The developer shall document major processes, including bibliographic import/export, authority validation, and standard reports.

**Reason:** Merged into REQ-116; duplicate concept was already captured there.

**Sources:**
- `early_draft_srs_galecia.txt`
- `meeting_tech_subcommittee_2009-06-30.txt`

### Discarded candidate

**Original statement:** The management reporting requirements shall not constrain or redefine day-to-day OPAC and circulation-client functionality.

**Reason:** Discarded because it is a scope clarification already covered conservatively by REQ-112 (OPAC isolation), and keeping it would be a redundant non-functional boundary statement rather than a unique requirement.

**Sources:**
- `meeting_minutes/meeting_2009-03-15_minutes.txt`
