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
After which you run the `pulumi` demo using:
```
./entrypoint.sh
```
With the expected output of:
```
Logged in to f813025ee57a as root (postgres://fastramqpi:fastramqpi@db:5432/fastramqpi?sslmode=disable)
Previewing update (test):
     Type                 Name       Plan
 +   pulumi:pulumi:Stack  demo-test  create

Outputs:
    exp_static: "foo"

Resources:
    + 1 to create
```
Showing that `pulumi` is running correctly.
