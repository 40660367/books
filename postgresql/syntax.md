# PostgreSQL 语法

可以使用`help`语句查看所有postgreSQL语句的语法。 按照以下步骤查看PostgreSQL中所有语句的语法。

- 使用以下语句查看特定语句的语法。 postgres-＃\ help＆

## 所有PostgreSQL语句

在这里，我们提供了所有postgreSQL语句及其语法的列表：

**ABORT语句：**

语法：

```sql
ABORT [ WORK | TRANSACTION ]
```

**ALTER AGGREGATE语句：**

语法：

```sql
ALTER AGGREGATE name ( type ) RENAME TO new_name  
ALTER AGGREGATE name ( type ) OWNER TO new_owner
```

**ALTER CONVERSION语句：**

语法：

```sql
ALTER CONVERSION name RENAME TO new_name  
ALTER CONVERSION name OWNER TO new_owner
```

**ALTER DATABASE语句：**

语法：

```sql
ALTER DATABASE name SET parameter { TO | = } { value | DEFAULT }  
ALTER DATABASE name RESET parameter  
ALTER DATABASE name RENAME TO new_name  
ALTER DATABASE name OWNER TO new_owner
```

**ALTER DOMAIN语句：**

语法：

```sql
ALTER DOMAIN name { SET DEFAULT expression | DROP DEFAULT }  
ALTER DOMAIN name { SET | DROP } NOT NULL  
ALTER DOMAIN name ADD domain_constraint  
ALTER DOMAIN name DROP CONSTRAINT constraint_name [ RESTRICT | CASCADE ]  
ALTER DOMAIN name OWNER TO new_owner
```

**ALTER FUNCTION语句：**

语法：

```sql
ALTER FUNCTION name ( [ type [, ...] ] ) RENAME TO new_name  
ALTER FUNCTION name ( [ type [, ...] ] ) OWNER TO new_owner
```

**ALTER GROUP语句：**

语法：

```sql
ALTER GROUP groupname ADD USER username [, ... ]  
ALTER GROUP groupname DROP USER username [, ... ]  
ALTER GROUP groupname RENAME TO new_name
```

**ALTER INDEX语句：**

语法：

```sql
ALTER INDEX name OWNER TO new_owner  
ALTER INDEX name SET TABLESPACE indexspace_name  
ALTER INDEX name RENAME TO new_name
```

**ALTER LANGUAGE语句：**

语法：

```sql
ALTER LANGUAGE name RENAME TO new_name
```

**ALTER OPERATOR语句：**

语法：

```sql
ALTER OPERATOR name ( { lefttype | NONE } , { righttype | NONE } )  
OWNER TO new_owner
```

**ALTER OPERATOR CLASS语句：**

语法：

```sql
ALTER OPERATOR CLASS name USING index_method RENAME TO new_name  
ALTER OPERATOR CLASS name USING index_method OWNER TO new_owner
```

**ALTER SCHEMA语句：**

语法：

```sql
ALTER SCHEMA name RENAME TO new_name  
ALTER SCHEMA name OWNER TO new_owner
```

**ALTER SEQUENCE语句：**

语法：

```sql
ALTER SEQUENCE name [ INCREMENT [ BY ] increment ]  
[ MINVALUE minvalue | NO MINVALUE ]  
[ MAXVALUE maxvalue | NO MAXVALUE ]  
[ RESTART [ WITH ] start ] [ CACHE cache ] [ [ NO ] CYCLE ]
```

**ALTER TABLE语句：**

语法：

```sql
ALTER TABLE [ ONLY ] name [ * ]  
action [, ... ]  
ALTER TABLE [ ONLY ] name [ * ]  
RENAME [ COLUMN ] column TO new_column  
ALTER TABLE name  
RENAME TO new_name
```

**ALTER TABLESPACE语句：**

语法：

```sql
ALTER TABLESPACE name RENAME TO new_name  
ALTER TABLESPACE name OWNER TO new_owner
```

**ALTER TRIGGER语句：**

语法：

```sql
ALTER TRIGGER name ON table RENAME TO new_name
```

**ALTER TYPE语句：**

语法：

```sql
ALTER TYPE name OWNER TO new_owner
```

**ALTER USER语句：**

语法：

```sql
ALTER USER name [ [ WITH ] option [ ... ] ]  
ALTER USER name RENAME TO new_name  
ALTER USER name SET parameter { TO | = } { value | DEFAULT }  
ALTER USER name RESET parameter
```

**ANALYSE语句：**

语法：

```sql
ANALYZE [ VERBOSE ] [ table [ (column [, ...] ) ] ]
```

**BEGIN语句：**

语法：

```sql
BEGIN [ WORK | TRANSACTION ] [ transaction_mode [, ...] ]
```

**CHECKPOINT语句：**

语法：

```sql
CHECKPOINT
```

**CLOSE语句：**

语法：

```sql
CLOSE name
```

**CLUSTER语句：**

语法：

```sql
CLUSTER index_name ON table_name  
CLUSTER table_name  
CLUSTER
```

**COMMIT语句：**

语法：

```sql
COMMIT [ WORK | TRANSACTION ]
```

**COPY语句：**

语法：

```sql
COPY table_name [ ( column [, ...] ) ]  
FROM { 'filename' | STDIN }  
[ [ WITH ]  
[ BINARY ]  
[ OIDS ]  
[ DELIMITER [ AS ] 'delimiter' ]  
[ NULL [ AS ] 'null string' ]  
[ CSV [ QUOTE [ AS ] 'quote' ]  
[ ESCAPE [ AS ] 'escape' ]  
[ FORCE NOT NULL column [, ...] ]  
COPY table_name [ ( column [, ...] ) ]  
TO { 'filename' | STDOUT }  
[ [ WITH ]  
[ BINARY ]  
[ OIDS ]  
[ DELIMITER [ AS ] 'delimiter' ]  
[ NULL [ AS ] 'null string' ]  
[ CSV [ QUOTE [ AS ] 'quote' ]  
[ ESCAPE [ AS ] 'escape' ]  
[ FORCE QUOTE column [, ...] ]
```

 **CREATE AGGREGATE语句：**

语法：

```sql
CREATE AGGREGATE name (  
BASETYPE = input_data_type,  
SFUNC = sfunc,  
STYPE = state_data_type  
[ , FINALFUNC = ffunc ]  
[ , INITCOND = initial_condition ]  
)
```

 **CREATE CAST语句：**

语法：

```sql
CREATE CAST (source_type AS target_type)  
WITH FUNCTION func_name (arg_types)  
[ AS ASSIGNMENT | AS IMPLICIT ]  
CREATE CAST (source_type AS target_type)  
WITHOUT FUNCTION  
[ AS ASSIGNMENT | AS IMPLICIT ]
```

 **CREATE CONSTRAINT TRIGGER语句：**

语法：

```sql
CREATE CONSTRAINT TRIGGER name  
AFTER events ON  
table_name constraint attributes  
FOR EACH ROW EXECUTE PROCEDURE func_name ( args )
```

 **CREATE CONVERSION语句：**

语法：

```sql
CREATE [DEFAULT] CONVERSION name  
FOR source_encoding TO dest_encoding FROM func_name
```

 **CREATE DATABASE语句：**

语法：

```sql
CREATE DATABASE name  
[ [ WITH ] [ OWNER [=] db_owner ]  
[ TEMPLATE [=] template ]  
[ ENCODING [=] encoding ]  
[ TABLESPACE [=] tablespace ] ]
```

 **CREATE DOMAIN语句：**

语法：

```sql
CREATE DOMAIN name [AS] data_type  
[ DEFAULT expression ]  
[ constraint [ ... ] ]
```

 **CREATE FUNCTION语句：**

语法：

```sql
CREATE [ OR REPLACE ] FUNCTION name ( [ [ arg_name ] arg_type [, ...] ] )  
RETURNS ret_type  
{ LANGUAGE lang_name  
| IMMUTABLE | STABLE | VOLATILE  
| CALLED ON NULL INPUT | RETURNS NULL ON NULL INPUT | STRICT  
| [ EXTERNAL ] SECURITY INVOKER | [ EXTERNAL ] SECURITY DEFINER  
| AS 'definition'  
| AS 'obj_file', 'link_symbol'  
} ...  
[ WITH ( attribute [, ...] ) ]
```

 **CREATE GROUP语句：**

语法：

```sql
CREATE GROUP name [ [ WITH ] option [ ... ] ]  
Where option can be:  
SYSID gid  
| USER username [, ...]
```

 **CREATE INDEX语句：**

语法：

```sql
CREATE [ UNIQUE ] INDEX name ON table [ USING method ]  
( { column | ( expression ) } [ opclass ] [, ...] )  
[ TABLESPACE tablespace ]  
[ WHERE predicate ]
```

 **CREATE LANGUAGE语句：**

语法：

```sql
CREATE [ TRUSTED ] [ PROCEDURAL ] LANGUAGE name  
HANDLER call_handler [ VALIDATOR val_function ]
```

 **CREATE OPERATOR语句：**

语法：

```sql
CREATE OPERATOR name (  
PROCEDURE = func_name  
[, LEFTARG = left_type ] [, RIGHTARG = right_type ]  
[, COMMUTATOR = com_op ] [, NEGATOR = neg_op ]  
[, RESTRICT = res_proc ] [, JOIN = join_proc ]  
[, HASHES ] [, MERGES ]  
[, SORT1 = left_sort_op ] [, SORT2 = right_sort_op ]  
[, LTCMP = less_than_op ] [, GTCMP = greater_than_op ]  
)
```

 **CREATE OPERATOR CLASS语句：**

语法：

```sql
CREATE OPERATOR CLASS name [ DEFAULT ] FOR TYPE data_type  
USING index_method AS  
{ OPERATOR strategy_number operator_name [ ( op_type, op_type ) ] [ RECHECK ]  
| FUNCTION support_number func_name ( argument_type [, ...] )  
| STORAGE storage_type  
} [, ... ]
```

 **CREATE RULE语句：**

语法：

```sql
CREATE [ OR REPLACE ] RULE name AS ON event  
TO table [ WHERE condition ]  
DO [ ALSO | INSTEAD ] { NOTHING | command | ( command ; command ... ) }
```

 **CREATE SCHEMA语句：**

语法：

```sql
CREATE SCHEMA schema_name  
[ AUTHORIZATION username ] [ schema_element [ ... ] ]  
CREATE SCHEMA AUTHORIZATION username  
[ schema_element [ ... ] ]
```

 **CREATE SEQUENCE语句：**

语法：

```sql
CREATE [ TEMPORARY | TEMP ] SEQUENCE name  
[ INCREMENT [ BY ] increment ]  
[ MINVALUE minvalue | NO MINVALUE ]  
[ MAXVALUE maxvalue | NO MAXVALUE ]  
[ START [ WITH ] start ] [ CACHE cache ] [ [ NO ] CYCLE ]
```

 **CREATE TABLE语句：**

语法：

```sql
CREATE [ [ GLOBAL | LOCAL ] { TEMPORARY | TEMP } ] TABLE table_name (  
{ column_name data_type [ DEFAULT default_expr ] [ column_constraint [ ... ] ]  
| table_constraint  
| LIKE parent_table [ { INCLUDING | EXCLUDING } DEFAULTS ] } [, ... ]  
)  
[ INHERITS ( parent_table [, ... ] ) ]  
[ WITH OIDS | WITHOUT OIDS ]  
[ ON COMMIT { PRESERVE ROWS | DELETE ROWS | DROP } ]  
[ TABLESPACE tablespace ]
```

 **CREATE TABLE AS语句：**

语法：

```sql
CREATE [ [ GLOBAL | LOCAL ] { TEMPORARY | TEMP } ] TABLE table_name  
[ (column_name [, ...] ) ] [ [ WITH | WITHOUT ] OIDS ]  
AS query
```

 **CREATE TABLESPACE语句：**

语法：

```sql
CREATE TABLESPACE tablespace_name [ OWNER username ] LOCATION 'directory'
```

 **CRFEATE TRIGGER语句：**

语法：

```sql
CREATE TRIGGER name { BEFORE | AFTER } { event [ OR ... ] }  
ON table [ FOR [ EACH ] { ROW | STATEMENT } ]  
EXECUTE PROCEDURE func_name ( arguments )
```

 **CREATE TYPE语句：**

语法：

```sql
CREATE TYPE name AS  
( attribute_name data_type [, ... ] )  
CREATE TYPE name (  
INPUT = input_function,  
OUTPUT = output_function  
[ , RECEIVE = receive_function ]  
[ , SEND = send_function ]  
[ , ANALYZE = analyze_function ]  
[ , INTERNALLENGTH = { internal_length | VARIABLE } ]  
[ , PASSEDBYVALUE ]  
[ , ALIGNMENT = alignment ]  
[ , STORAGE = storage ]  
[ , DEFAULT = default ]  
[ , ELEMENT = element ]  
[ , DELIMITER = delimiter ]  
)
```

 **CREATE USER语句：**

语法：

```sql
CREATE USER name [ [ WITH ] option [ ... ] ]
```

 **CREATE VIEW语句：**

语法：

```sql
CREATE [ OR REPLACE ] VIEW name [ ( column_name [, ...] ) ] AS query
```

 **DEALLOCATE语句：**

语法：

```sql
DEALLOCATE [ PREPARE ] plan_name
```

 **DECLARE语句：**

语法：

```sql
DECLARE name [ BINARY ] [ INSENSITIVE ] [ [ NO ] SCROLL ]  
CURSOR [ { WITH | WITHOUT } HOLD ] FOR query  
[ FOR { READ ONLY | UPDATE [ OF column [, ...] ] } ]
```

 **DELETE语句：**

语法：

```sql
DELETE FROM [ ONLY ] table [ WHERE condition ]
```

 **DROP AGGREGATE语句：**

语法：

```sql
DROP AGGREGATE name ( type ) [ CASCADE | RESTRICT ]
```

 **DROP CAST语句：**

语法：

```sql
DROP CAST (source_type AS target_type) [ CASCADE | RESTRICT ]
```

 **DROP CONVERSION语句：**

语法：

```sql
DROP CONVERSION name [ CASCADE | RESTRICT ]
```

 **DROP DATABASE语句：**

语法：

```sql
DROP DATABASE name
```

 **DROP DOMAIN语句：**

语法：

```sql
DROP DOMAIN name [, ...] [ CASCADE | RESTRICT ]
```

 **DROP FUNCTION语句：**

语法：

```sql
DROP FUNCTION name ( [ type [, ...] ] ) [ CASCADE | RESTRICT ]
```

 **DROP GROUP语句：**

语法：

```sql
DROP GROUP name
```

 **DROP INDEX语句：**

语法：

```sql
DROP INDEX name [, ...] [ CASCADE | RESTRICT ]
```

 **DROP LANGUAGE语句：**

语法：

```sql
DROP [ PROCEDURAL ] LANGUAGE name [ CASCADE | RESTRICT ]
```

 **DROP OPERATOR语句：**

语法：

```sql
DROP OPERATOR name ( { left_type | NONE } , { right_type | NONE } )  
[ CASCADE | RESTRICT ]
```

 **DROP OPERATOR CLASS语句：**

语法：

```sql
DROP OPERATOR CLASS name USING index_method [ CASCADE | RESTRICT ]
```

 **DROP RULE语句：**

语法：

```sql
DROP RULE name ON relation [CASCADE | RESTRICT ]
```

 **DROP SCHEMA语句：**

语法：

```sql
DROP SCHEMA name [, ...] [ CASCADE | RESTRICT ]
```

 **DROP SEQUENCE语句：**

语法：

```sql
DROP SEQUENCE name [, ...] [ CASCADE | RESTRICT ]
```

 **DROP TABLE语句：**

语法：

```sql
DROP TABLE name [, ...] [ CASCADE | RESTRICT ]
```

 **DROP TABLESPACE语句：**

语法：

```sql
DROP TABLESPACE tablespace_name
```

 **DROP TRIGGER语句：**

语法：

```sql
DROP TRIGGER name ON table [ CASCADE | RESTRICT ]
```

 **DROP TYPE语句：**

语法：

```sql
DROP TYPE name [, ...] [ CASCADE | RESTRICT ]
```

 **DROP USER语句：**

语法：

```sql
DROP USER name
```

 **DROP VIEW语句：**

语法：

```sql
DROP VIEW name [, ...] [ CASCADE | RESTRICT ]
```

 **END语句：**

语法：

```sql
END [ WORK | TRANSACTION ]
```

 **EXECUTE语句：**

语法：

```sql
EXECUTE plan_name [ (parameter [, ...] ) ]
```

 **EXPLAIN语句：**

语法：

```sql
EXPLAIN [ ANALYZE ] [ VERBOSE ] statement
```

 **FETCH语句：**

语法：

```sql
FETCH [ direction { FROM | IN } ] cursor_name
SQL
```

 **INSERT语句：**

语法：

```sql
INSERT INTO table [ ( column [, ...] ) ]  
{ DEFAULT VALUES | VALUES ( { expression | DEFAULT } [, ...] ) | query }
```

 **LISTEN语句：**

语法：

```sql
LISTEN name
```

 **LOAD语句：**

语法：

```sql
LOAD 'filename'
```

 **LOCK语句：**

语法：

```sql
LOCK [ TABLE ] name [, ...] [ IN lock_mode MODE ] [ NOWAIT ]
```

 **MOVE语句：**

语法：

```sql
MOVE [ direction { FROM | IN } ] cursor_name
```

 **NOTIFY语句：**

语法：

```sql
NOTIFY name
```

 **PREPARE语句：**

语法：

```sql
PREPARE plan_name [ (data_type [, ...] ) ] AS statement
```

 **REINDEX语句：**

语法：

```sql
REINDEX { DATABASE | TABLE | INDEX } name [ FORCE ]
```

 **RESET语句：**

语法：

```sql
RESET name  
RESET ALL
```

 **ROLLBACK语句：**

语法：

```sql
ROLLBACK [ WORK | TRANSACTION ]
```

 **ROLLBACK TO SAVEPOINT语句：**

语法：

```sql
ROLLBACK [ WORK | TRANSACTION ] TO [ SAVEPOINT ] savepoint_name
```

 **SAVEPOINT语句：**

语法：

```sql
SAVEPOINT savepoint_name
```

 **SELECT语句：**

语法：

```sql
SELECT [ ALL | DISTINCT [ ON ( expression [, ...] ) ] ]  
* | expression [ AS output_name ] [, ...]  
[ FROM from_item [, ...] ]  
[ WHERE condition ]  
[ GROUP BY expression [, ...] ]  
[ HAVING condition [, ...] ]  
[ { UNION | INTERSECT | EXCEPT } [ ALL ] select ]  
[ ORDER BY expression [ ASC | DESC | USING operator ] [, ...] ]  
[ LIMIT { count | ALL } ]  
[ OFFSET start ]  
[ FOR UPDATE [ OF table_name [, ...] ] ]
```

 **SELECT INTO语句：**

语法：

```sql
SELECT [ ALL | DISTINCT [ ON ( expression [, ...] ) ] ]  
* | expression [ AS output_name ] [, ...]  
INTO [ TEMPORARY | TEMP ] [ TABLE ] new_table  
[ FROM from_item [, ...] ]  
[ WHERE condition ]  
[ GROUP BY expression [, ...] ]  
[ HAVING condition [, ...] ]  
[ { UNION | INTERSECT | EXCEPT } [ ALL ] select ]  
[ ORDER BY expression [ ASC | DESC | USING operator ] [, ...] ]  
[ LIMIT { count | ALL } ]  
[ OFFSET start ]  
[ FOR UPDATE [ OF table_name [, ...] ] ]
```

 **SET语句：**

语法：

```sql
SET [ SESSION | LOCAL ] name { TO | = } { value | 'value' | DEFAULT }  
SET [ SESSION | LOCAL ] TIME ZONE { time_zone | LOCAL | DEFAULT }
```

 **SET CONSTRAINTS语句：**

语法：

```sql
SET CONSTRAINTS { ALL | name [, ...] } { DEFERRED | IMMEDIATE }
```

 **SET TRANSACTION语句：**

语法：

```sql
SET TRANSACTION transaction_mode [, ...]  
SET SESSION CHARACTERISTICS AS TRANSACTION transaction_mode [, ...]
```

 **SHOW语句：**

语法：

```sql
SHOW name  
SHOW ALL
```

 **START TRANSACTION语句：**

语法：

```sql
START TRANSACTION [ transaction_mode [, ...] ]
```

 **TRUNCATE TABLE语句：**

语法：

```sql
TRUNCATE [ TABLE ] name
```

 **UPDATE语句：**

语法：

```sql
UPDATE [ ONLY ] table SET column = { expression | DEFAULT } [, ...]  
[ FROM from_list ]  
[ WHERE condition ]
```