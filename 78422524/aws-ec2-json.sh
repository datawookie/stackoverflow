#!/bin/bash

VPC_ID=vpc-05ae0495871281736

NETWORK_INTERFACE=$(aws ec2 describe-network-interfaces --filters Name=vpc-id,Values="${VPC_ID}" --output json | jq -r '[.NetworkInterfaces[] | {AvailabilityZone, Description, Groups}]')

echo $NETWORK_INTERFACE
