print("--- Starting Network Scan ---")
for server_id in range(101,106):
    if server_id == 104:
        print (f"WARNING :server {server_id} is offline!")
    else:
        print(f"server {server_id} is online and running.")
        print("---Network scan complete---")