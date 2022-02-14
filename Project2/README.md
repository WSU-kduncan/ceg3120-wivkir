"Part 1 - Build a VPC"
- Create a VPC
  - Tag it with "YOURLASTNAME-VPC"
  - Specify a /24 private IP address range
  - Description
  - Screenshot 


- Create a subnet

  - Tag it with "YOURLASTNAME-Subnet"
  - Specify a /28 private IP address range
  - Attach it to your VPC
  - Description
  - Screenshot


- Create an internet gateway

  - Tag it with "YOURLASTNAME-gw"
  - Attach it to your VPC
  - Description
  - Screenshot


- Create a route table

  - Tag it with "YOURLASTNAME-routetable"
  - Attach it to your VPC
  - Associate it with your subnet
  - Add a routing table rule that sends traffic to all destinations to your internet gateway
  - Description
  - Screenshot


- Create a security group

  - Tag it with "YOURLASTNAME-sg"
  - Allow SSH for a set of trusted networks including:
    - Your home / where you usually connect to your instances from
    - Wright State (addresses starting with 130.108)
    - Instances within the VPC
  - Attach it to your VPC
  - Image should include your Inbound rules
  - Description
  - Screenshot


- (If necessary, else skip) Create a key pair

"Part 2 - EC2 instances"
- Create a new instance. Give a write up of the following information:
  - AMI selected
    - default username of the instance type selected
  - Instance type selected
- Attach the instance to your VPC. As discussed there are different pathways to doing this. Say how you did it.
- Determine whether a Public IPv4 address will be auto-assigned to the instance. Justify your choice to do so (or not do so)
  - NOTE - in the next few steps, you will be required to request an Elastic IP address and associate it to the instance. Factor that in to your discussion here.
- Attach a volume to your instance. As discussed there are different pathways to doing this. Say how you did it.
- Tag your instance with a "Name" of "YOURLASTNAME-instance". Say how you did it
- Associate your security group, "YOURLASTNAME-sg" to your instance. Say how you did it.
- Reserve an Elastic IP address. Tag it with "YOURLASTNAME-EIP". Associate the Elastic IP with your instance. Say how you did it.
- Create a screenshot your instance details and add it to your project write up. Example below: sample instance details
- ssh in to your instance. Change the hostname to "YOURLASTNAME-AMI" where AMI is some version of the AMI you chose. Say how you did it.
  - It is wise to copy config files you are about to change to filename.old For /etc/hostname, for example, I would first copy the current hostname file to /etc/hostname.old
  - You should not change permissions on any files you are modifying. They are system config files. You may need to access them with adminisrative privileges.
  - Here is a helpful resource: https://www.tecmint.com/set-hostname-permanently-in-linux/ I did not modify /etc/hosts on mine - do so or not as you wish.
- Create a screenshot your ssh connection to your instance and add it to your project write up - make sure it shows your new hostname.

