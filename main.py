#AWS_ACCESS_KEY_ID: AKIA4OKQNYEHHBQI25EX
#AWS_SECRET_ACCESS_KEY: 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
import boto3

region = "eu-west-1"

instance1 = 'i-0c110e8bd99b97f9b'
#print(instance1.tags)

ec2 = boto3.resource('ec2', region_name=region)
"""
for instance in ec2.instances.all():
    print("Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState:{5}\n".format(
    instance.id, instance.platform, instance.instance_type,
    instance.public_ip_address, instance.image.id, instance.state
        )
    )
"""

for instance in ec2.instances.all():

    #print(type(instance.tags))
    print("{} : {}".format(instance.id, instance.state["Code"]))
    #print(instance.tags)
    if instance.tags == None:
        print(instance.id)
    else:
        lis = instance.tags[0]
        print(lis['Key'])
#print("Id: {0}\n State: {5}\n".format(instance.id, instance.state))


###MAIN CODE###
"""
for instance in ec2.instances.all():
    lis = instance.tags[0]
    if lis['Key'] == "k8s.io/role/master" and instance.state["Code"] == 16:
        ec2.Instance(instance.id).stop()
"""

