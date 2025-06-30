import json

def keysStartingWith(theString, theDictionary):
    return dict(filter(lambda item: item[0].startswith(theString), theDictionary.items()))

"""
def nested(prefix, theDictionary):
    for key in theDictionary.keys():
        #print(key)
        if(key.startswith(prefix)):
            thisThing = key.replace(prefix,"")
            return key, thisThing
    print("fart")
"""
def hasKey(thisKey, thisDictionary):
    # https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary
    return thisDictionary[thisKey] if thisKey in thisDictionary else ""

with open("config.boot.json", mode="r", encoding="utf-8") as read_file:
    jsonF = json.load(read_file)

    #print(json.dumps(jsonF["service"]["dhcp-server"], indent=4))
    # https://www.geeksforgeeks.org/python/python-prefix-key-match-in-dictionary/
    # gets key that startswith
    #{key: val for key, val in test_dict.items()
    #   if key.startswith(test_pref)}
    #dict(filter(lambda item: item[0].startswith(test_pref), test_dict.items()))
    #print(json.dumps(jsonF["service"]["dhcp-server"], indent=4))
    ##print(json.dumps(jsonF["service"]["dhcp-server"]dict(filter(lambda item: item[0].startswith("shared"), print(json.dumps(jsonF["service"]["dhcp-server"].items())))), indent=4))
    #res = {key: val for key, val in jsonF["service"]["dhcp-server"].items()
    #   if key.startswith("shared")}
    #res = dict(filter(lambda item: item[0].startswith("shared"), jsonF["service"]["dhcp-server"].items()))
    #netDict = keysStartingWith("shared", jsonF["service"]["dhcp-server"])
    #print(json.dumps(netDict, indent=4))

    print("Networks and DHCP Reservations")
    # https://stackoverflow.com/questions/70782902/best-way-to-navigate-a-nested-json-in-python
    # https://www.geeksforgeeks.org/python/python-accessing-key-value-in-dictionary/
    #print(type(res))
    network_name_prefix = "shared-network-name "
    subnet_prefix = "subnet "
    start_prefix = "start "
    reservation_desc_prefix = "static-mapping "
    reservation_ip_address_prefix = "ip-address"
    reservation_mac_address_prefix = "mac-address"
    for key in jsonF["service"]["dhcp-server"].keys():
        #print(key)
        if(key.startswith(network_name_prefix)):
            network_name = key.replace(network_name_prefix,"")
            #print(key, network_name)
            #print(key.replace(network_name_prefix,""))
            #print(network_name)

            for key2 in jsonF["service"]["dhcp-server"][key].keys():
                if(key2.startswith(subnet_prefix)):
                    subnet = key2.replace(subnet_prefix,"")
                    #print(key2, "|", subnet)
                    default_router = jsonF["service"]["dhcp-server"][key][key2]["default-router"]
                    lease = jsonF["service"]["dhcp-server"][key][key2]["lease"]
                        #"start 192.168.1.38": {
                        #"stop": "192.168.1.243"
                    for key3 in jsonF["service"]["dhcp-server"][key][key2].keys():
                        if(key3.startswith(start_prefix)):
                            start = key3.replace(start_prefix,"")
                            #print(key3, "|", start)
                            stop = jsonF["service"]["dhcp-server"][key][key2][key3]["stop"]
                    for key4 in jsonF["service"]["dhcp-server"][key][key2].keys():
                        if(key4.startswith(reservation_desc_prefix)):
                            reservation_desc = key4.replace(reservation_desc_prefix,"")
                            #print(key4, "|", start)
                            reservation_ip_address = jsonF["service"]["dhcp-server"][key][key2][key4][reservation_ip_address_prefix]
                            reservation_mac_address = jsonF["service"]["dhcp-server"][key][key2][key4][reservation_mac_address_prefix]

                            print("|".join(["reservation",reservation_desc, reservation_ip_address, reservation_mac_address]))

                    #print("|".join(["network",key,network_name,key2, subnet, default_router,lease, key3, start, stop]))
                    print("|".join(["network",network_name, subnet, default_router,lease, start, stop]))

    print("Physical Interfaces")

    ethernet_prefix = "ethernet "
    for key in jsonF["interfaces"].keys():
        #print(key)
        if(key.startswith(ethernet_prefix)):
            ethernet_port = key.replace(ethernet_prefix,"")
            #ethernet_port_address = jsonF["interfaces"][key]["address"] if "address" in jsonF["interfaces"][key] else ""
            ethernet_port_address = hasKey("address", jsonF["interfaces"][key])
            #ethernet_port_description = jsonF["interfaces"][key]["description"] if "description" in jsonF["interfaces"][key] else ""
            ethernet_port_description = hasKey("description", jsonF["interfaces"][key])
            print("|".join(["interface", key, ethernet_port, ethernet_port_address, ethernet_port_description]))
            #

    print("Virtual Interfaces")

    virtual_interface_prefix = "vif "
    for key in jsonF["interfaces"]["ethernet eth7"].keys():
        #print("1111", key)
        if(key.startswith(virtual_interface_prefix)):
            #print("2222", key)
            vlan = key.replace(virtual_interface_prefix,"")
            #print(jsonF["interfaces"]["ethernet eth7"][key])
            vlan_router_address = hasKey("address", jsonF["interfaces"]["ethernet eth7"][key])
            vlan_description = hasKey("description", jsonF["interfaces"]["ethernet eth7"][key])
            print("|".join(["interface", key, vlan, vlan_router_address, vlan_description]))

    print("Load-Balance")

    group_prefix = "group "
    interface_prefix = "interface "
    for key in jsonF["load-balance"].keys():
        #print(key)
        if(key.startswith(group_prefix)):
            #print("1111", key)
            group = key.replace(virtual_interface_prefix,"")
            for key2 in jsonF["load-balance"][key].keys():
                #print(key2)
                if(key2.startswith(interface_prefix)):
                    #print("2222", key2)
                    interface = key2.replace(virtual_interface_prefix,"")
                    failover_only = hasKey("failover-only", jsonF["load-balance"][key][key2])

                    print("|".join(["load-balance", group, interface, failover_only]))


    print("Port-Fowards")

    port_forward_prefix = "vif "
    rule_prefix = "rule "
    for key in jsonF["port-forward"].keys():
        #print(key)
        if(key.startswith(port_forward_prefix)):
            #print(key)
            port_forward = key.replace(port_forward_prefix,"")
            #print(jsonF["interfaces"]["ethernet eth7"][key])
            vlan_router_address = hasKey("address", jsonF["interfaces"]["ethernet eth7"][key])
            vlan_description = hasKey("description", jsonF["interfaces"]["ethernet eth7"][key])
            print("|".join(["port-forward", key, vlan, vlan_router_address, vlan_description]))




print("End of program")

"""

    "port-forward": {
        "auto-firewall": "enable",
        "hairpin-nat": "enable",
        "lan-interface": "eth7",
        "rule 1": {
            "description": "ACM Port Forwarding",
            "forward-to": {
                "address": "10.200.117.224",
                "port": "443"
            },
            "original-port": "443",
            "protocol": "tcp"
        },
        "rule 2": {
            "description": "",
            "forward-to": {
                "address": "10.200.117.224",
                "port": "80"
            },
            "original-port": "80",
            "protocol": "tcp"
        },
        "wan-interface": "eth0"
"""
