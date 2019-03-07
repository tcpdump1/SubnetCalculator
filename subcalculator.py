#https://networkengineering.stackexchange.com/questions/7106/how-do-you-calculate-the-prefix-network-subnet-and-host-numbers
#https://www.pluralsight.com/blog/it-ops/simplify-routing-how-to-organize-your-network-into-smaller-subnets

def subnetcalculator(ipaddress, subnetmask):
    
    
##### Split the network and subnet mask into a list e.g [192,168,50.40]

    ipaddress_list = map(int, ipaddress.split("."))
    sub_list = map(int, subnetmask.split("."))
    
#### Convert the integers in each list into binary 8 bits format e.g [00001000,11110000,11110000,11110000]
    ipaddress_list = [format(x,'08b') for x in ipaddress_list]
    sub_list = [format(x,'08b') for x in sub_list]

#### Join these lists into a string like this "00001000111100001111000011110000". Why ? so we can perform an AND operation to get the subnet
#### For example, lets say we want to find the subnet address of 144.68.50.4 with a subnet mask of 255.255.255.248
#### Eg. ipaddress_string = 10010000010001000011001000000100 ==> 144.68.50.4
####     subnetmask_string = 11111111111111111111111111111000 ==> 255.255.255.248
    ipaddress_string = "".join(ipaddress_list)
    subnetmask_string = "".join(sub_list)
    
    
#### Get the host portion of the subnetmask by switching the bits for the host portion to 1 and switching the bits for network portion to 0. This is used to get the broadcast IP address. If subnet mask = 255.255.255.248, host_string is 00000000000000000000000000000111
    host_string = ""
    for i in range(len(subnetmask_string)):
        if subnetmask_string[i] == "1":
            host_string += "0"
        else:
            host_string += "1"
    
          
#### Now the action begins    
    netadd = ""
    broadadd = ""
    

#### We loop through ipaddress_string and subnetmask_string and perform an AND operation to get the network address of the network. 1 and 1 = 1, 0 and 1 = 0, 1 and 0 = 0, 0 and 0 = 0
#### For example:
####  ipaddress_string = 10010000010001000011001000000100 ==> 144.68.50.4
####  AND
####  subnetmask_string = 11111111111111111111111111111000 ==> 255.255.255.248
#### Push the value of the AND operation to a variable called netadd and this becomes the network address
    for i in range(len(ipaddress_string)):
        for j in range(len(subnetmask_string)):
            if i == j:          
                if ipaddress_string[i] == subnetmask_string[j] and ipaddress_string[i] == "1":
                    netadd += "1"               
                elif ipaddress_string[i] == subnetmask_string[j] and ipaddress_string[i] == "0":
                    netadd += "0"               
                else:
                    netadd += "0"
#### Convert the binary value into an integer and place that in a list called network_add                 
    network_add = [str(int(netadd[0:8],2)), str(int(netadd[8:16],2)), str(int(netadd[16:24],2)), str(int(netadd[24:32],2))]


    
    
    
    
### We loop through ipaddress_string and host_string and perform an OR operation to get the broadcast address of the network. 1 or 1 = 1, 0 or 1 = 1, 1 or 0 = 1, 0 and 0 = 0
#### For example:
####  ipaddress_string = 10010000010001000011001000000100 ==> 144.68.50.4
####  AND
####  host_string = 00000000000000000000000000000111 ==> 255.255.255.248
#### Push the value of the OR operation to a variable called broadadd and this becomes the broadcast address      
    for i in range(len(ipaddress_string)):
        for j in range(len(host_string)):
            if i == j:          
                if ipaddress_string[i] == "1":
                    broadadd += "1"               
                elif host_string[j] == "1":
                    broadadd += "1"               
                else:
                    broadadd += "0"
#### Convert the binary value into an integer and place that in a list called broadcast_add
    broadcast_add = [str(int(broadadd[0:8],2)), str(int(broadadd[8:16],2)), str(int(broadadd[16:24],2)), str(int(broadadd[24:32],2))]
    

    
#### Time to find the first address in the subnet
#### To find the first address, switch the last bit of netadd to 1
    firstadd = [x for x in netadd]
    firstadd = "".join(firstadd[0:31]) + "1"
#### Convert the binary value into an integer and place that in a list called first_add
    first_add = [str(int(firstadd[0:8],2)), str(int(firstadd[8:16],2)), str(int(firstadd[16:24],2)), str(int(firstadd[24:32],2))]
    
    
    
#### Time to find the last address in the subnet
#### To find the last address, switch the last bit of broadadd to 0  
    lastadd = [x for x in broadadd]
    lastadd = "".join(lastadd[0:31]) + "0"
#### Convert the binary value into an integer and place that in a list called last_add
    last_add = [str(int(lastadd[0:8],2)), str(int(lastadd[8:16],2)), str(int(lastadd[16:24],2)), str(int(lastadd[24:32],2))]
    

#### Join the lists into a string and print    
    print "The network address is %s" %(".".join(network_add))
    print "The broadcast address is %s" %(".".join(broadcast_add)) 
    print "The first IP address in this subnet is %s" %(".".join(first_add)) 
    print "The last IP address in this subnet is %s" %(".".join(last_add))

subnetcalculator("144.68.50.4", "255.255.255.248")