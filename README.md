# pulumi_mo

Dynamic Pulumi provider for OS2mo

## Getting started

To start the demo environment simply run:
```
docker compose up --build
```
And wait for the containers to start:
```
...
[+] Running 3/3
 ✔ pulumi_mo                        Built       0.0s
 ✔ Container pulumi_mo-db-1         Running     0.0s
 ✔ Container pulumi_mo-pulumi_mo-1  Running     0.0s
```
Then you can enter into the `pulumi` container using:
```
docker compose exec pulumi_mo /bin/bash
```
After which you can either run the tests using:
```
poetry run pytest tests
```
With the expected output of all tests passing.
Or you can run the `pulumi` demo using:
```
./entrypoint.sh
```
With the expected output of:
```
Logged in to f813025ee57a as root (postgres://fastramqpi:fastramqpi@db:5432/fastramqpi?sslmode=disable)
Previewing update (test):
     Type                 Name       Plan
 +   pulumi:pulumi:Stack  demo-test  create
 +   ├─ pulumi-python:dynamic:Resource  suila      create
 +   ├─ pulumi-python:dynamic:Resource  alya        create
 +   └─ pulumi-python:dynamic:Resource  suila:alya  create

Outputs:
    actor_uuid: "d1fec000-baad-c0de-0000-004449504558"
    itsystem_uuid: [unknown]
    ituser_uuid  : [unknown]
    person_uuid  : [unknown]

Resources:
    + 4 to create
```
Showing that `pulumi` is running correctly.

Additionally you can now run `pulumi up` to effectuate the changes.
In this case creating three resources in MO.
