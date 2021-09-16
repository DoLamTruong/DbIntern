CREATE TABLE driverlocation1 (
	id serial PRIMARY KEY,
	latitude double precision NOT NULL,
	longitude double precision NOT NULL,
	h3index bigint NOT NULL,
	driverid int NOT NULL,
    active bool NOT NULL
);
CREATE index on driverlocation2(h3index);
CREATE index on driverlocation2(driverid);

