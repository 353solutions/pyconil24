import sqlite3

schema_sql = """
CREATE TABLE IF NOT EXISTS rides (
    id VARCHAR(32), -- PRIMARY KEY
    driver_id VARCHAR(32),
    kind VARCHAR(16), -- regular, shared
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    distance REAL
);
"""

start_sql = """
INSERT INTO rides 
(id, driver_id, kind, start_time) 
VALUES
(:id, :driver_id, :kind, :start_time) 
;
"""

end_sql = """
UPDATE rides
SET 
    end_time = :end_time, 
    distance = :distance
WHERE
    id = :id AND
    distance IS NULL
;
"""

get_sql = """
SELECT
    id, driver_id, kind, start_time, end_time, distance
FROM
    rides
WHERE
    id = :id
"""


class DBError(Exception):
    pass


class DB:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(
            db_path,
            detect_types=sqlite3.PARSE_DECLTYPES,
            check_same_thread=False,
        )
        self.conn.row_factory = sqlite3.Row
        self.conn.execute(schema_sql)
        self.conn.commit()

    def close(self):
        if not self.conn:
            return

        self.conn.close()
        self.conn = None

    def start_ride(self, id, driver_id, kind, start_time):
        params = {
            'id': id,
            'driver_id': driver_id,
            'kind': kind,
            'start_time': start_time,
        }
        with self.conn as cur:
            cur.execute(start_sql, params)

    def end_ride(self, id, distance, end_time):
        params = {'id': id, 'end_time': end_time, 'distance': distance}
        with self.conn:
            cur = self.conn.execute(end_sql, params)
            num_changes = cur.rowcount

        if num_changes == 0:
            raise DBError(f'ride {id!r} does not exist or already ended')

    def get_ride(self, id):
        row = self.conn.execute(get_sql, {'id': id}).fetchone()
        return dict(row)
