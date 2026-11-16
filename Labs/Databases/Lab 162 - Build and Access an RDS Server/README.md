# Lab 162 — Build Your DB Server and Interact With Your DB

## Overview

This lab focused on provisioning an Amazon RDS for MySQL database, connecting to it from a Linux EC2 environment, creating a relational database and tables, inserting records, and querying the data with an `INNER JOIN`.

The work was completed in the AWS re/Start lab environment on 19 July 2026.

## Environment

- **AWS service:** Amazon RDS for MySQL
- **Compute/client environment:** Amazon EC2 running Amazon Linux 2
- **Database identifier:** `my-database`
- **DB instance class:** `db.t3.medium`
- **Region:** US West (Oregon), `us-west-2`
- **Database port:** TCP `3306`
- **Database access:** The RDS instance was configured as not publicly accessible.
- **Client:** MariaDB/MySQL command-line client, accessed through an SSH session using PuTTY

The lab used an EC2-based Linux environment as the database client and Amazon RDS as the managed database service.

## What I did

1. Reviewed the lab's database and compute requirements.
2. Provisioned and inspected the RDS for MySQL instance.
3. Connected to the Linux environment over SSH and prepared the database client.
4. Investigated connection, client compatibility, and SQL errors encountered during setup.
5. Created the `Vocareum_db` database and selected it as the active database.
6. Created and populated the `RESTART` and `CLOUD_PRACTITIONER` tables.
7. Queried the tables to verify the inserted records.
8. Used an `INNER JOIN` on the shared `Certification_ID` field to retrieve student IDs, student names, and certification dates.

## Troubleshooting and debugging

The lab involved several distinct classes of problems. I used the error messages and command output to identify where each failure was occurring rather than treating every failure as an RDS problem.

| Problem encountered | What the error indicated | Debugging lesson |
|---|---|---|
| `apt: command not found` | The Amazon Linux 2 environment did not use the attempted Debian/Ubuntu package command. | Check the operating system and use tools appropriate to that environment. |
| `mysql: command not found` | The database client was not yet available in the shell. | Confirm required client dependencies before attempting a database connection. |
| RDS connection timeout (`ERROR 2003`) | The client could not establish a TCP connection to the RDS endpoint at that point. | Separate network reachability problems from SQL and authentication problems. |
| `caching_sha2_password` plugin could not be loaded | The MariaDB 5.5.68 client lacked the requested authentication plugin. | Consider client/server authentication compatibility when connection attempts fail. |
| `--ssl-mode=VERIFY_IDENTITY` was reported as an unknown variable | The MariaDB client did not accept that MySQL-specific option. | Check which options the installed client actually supports instead of assuming clients are interchangeable. |
| `ERROR 1046: No database selected` | A table-creation statement was issued without an active database. | Create and select the intended database before creating tables. |
| `ERROR 1044: Access denied` on the `mysql` system database | The account did not have permission to create objects in the protected system database. | Create application/lab objects in an appropriate user database, not a system schema. |
| `ERROR 1146: Table ... CLOUD doesn't exist` | The table name in the `DESCRIBE` statement did not match the actual table name. | Read the exact object name and correct the SQL statement. |

The connection and client errors were followed by a working SQL session and successful query execution. The recovered evidence does not establish the exact configuration change that resolved every earlier connection/client error, so this write-up records the observed diagnosis and successful outcome without claiming an undocumented fix.

## SQL implementation and verification

I created the lab database and two related tables:

- `RESTART`
- `CLOUD_PRACTITIONER`

The tables were populated with ten student records and five certification records respectively. I verified the inserted data with `SELECT` queries and checked the record count.

The final task was to combine the two tables using their shared `Certification_ID` field:

```sql
SELECT
    RESTART.Student_ID,
    RESTART.Student_Name,
    CLOUD_PRACTITIONER.Certification_Date
FROM RESTART
INNER JOIN CLOUD_PRACTITIONER
    ON RESTART.Certification_ID = CLOUD_PRACTITIONER.Certification_ID
ORDER BY RESTART.Student_ID;
```

The query returned ten joined rows containing the requested student ID, student name, and certification date fields.

## Evidence

The screenshots directory is reserved for five concise pieces of evidence. The selected images will be added after visual review of the recovered archive.

1. **RDS environment** — the managed database configuration and relevant connection context.
2. **Troubleshooting** — representative client/connection diagnostics showing the investigation of setup failures.
3. **Database and table creation** — successful creation of `Vocareum_db` and its lab tables.
4. **Data verification** — populated table data and record-count validation.
5. **Final INNER JOIN** — the completed query and its ten-row result.

The goal is to show the technical progression and debugging decisions without reproducing every command or intermediate console state.

## Skills demonstrated

- Provisioning and inspecting an Amazon RDS for MySQL instance
- Connecting to a managed database from an EC2-hosted Linux environment
- Using SSH and a command-line SQL client
- Distinguishing network, client compatibility, authentication, and SQL errors
- Creating databases and relational tables
- Inserting and validating records
- Understanding database selection and schema permissions
- Writing an `INNER JOIN` using a shared key
- Using error messages as diagnostic evidence
