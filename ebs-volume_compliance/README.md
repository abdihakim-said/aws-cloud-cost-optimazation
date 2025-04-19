
# **AWS EBS Volume Compliance Automation**

## **Overview**
This repository contains a Lambda function script designed to enforce compliance for AWS EBS volumes by automatically converting newly created volumes to the `gp3` type. The script ensures that all EBS volumes adhere to organizational policies for cost optimization and performance.

---

## **Scenario**

### **Client Problem**
A SaaS company approached our consultancy with concerns about their rising AWS costs and inconsistent infrastructure standards. The client had the following challenges:
1. **High Storage Costs**: EBS volumes were being created with the default `gp2` type, which is more expensive than `gp3` for similar performance.
2. **Lack of Automation**: There was no automated mechanism to enforce compliance for newly created EBS volumes.
3. **Operational Overhead**: The DevOps team had to manually identify and modify non-compliant volumes, which was time-consuming and error-prone.

### **Solution**
To address these challenges, we implemented an **AWS Lambda function** that:
- Automatically detects the creation of new EBS volumes using **CloudWatch Events**.
- Converts non-compliant `gp2` volumes to the `gp3` type immediately after creation.
- Reduces manual intervention and ensures compliance with organizational policies.

---

## **How It Works**

1. **CloudWatch Event Rule**:
   - A CloudWatch Event Rule triggers the Lambda function whenever a new EBS volume is created.
   - The event payload contains the ARN of the newly created volume.

2. **Lambda Function**:
   - The Lambda function extracts the volume ID from the event payload.
   - It uses the AWS SDK (`boto3`) to modify the volume type to `gp3`.

3. **Automation**:
   - The entire process is automated, ensuring compliance without manual intervention.

---



## **Deployment Steps**

### **1. Create a CloudWatch Event Rule**
- Create a CloudWatch Event Rule to trigger the Lambda function on the `CreateVolume` API call.


### **2. Deploy the Lambda Function**
- Upload the script to an AWS Lambda function.
- Set the runtime to **Python 3.9** or later.
- Attach an IAM role with the following permissions:
  - `ec2:ModifyVolume`
  - `ec2:DescribeVolumes`

### **3. Test the Function**
- Use the AWS Lambda console to test the function with a sample event payload:

 

### **4. Monitor Logs**
- Check the Lambda function logs in **CloudWatch** to verify that the function is working as expected.

---

## **Benefits**

1. **Cost Optimization**:
   - Reduces storage costs by ensuring all EBS volumes use the `gp3` type, which is more cost-effective than `gp2`.

2. **Automation**:
   - Eliminates the need for manual intervention, saving time and reducing errors.

3. **Compliance Enforcement**:
   - Ensures all newly created EBS volumes adhere to organizational policies.

4. **Scalability**:
   - The solution is scalable and can handle large volumes of EBS creation events.

---

## **Example Use Case**

### **Before Automation**
- A developer creates an EBS volume with the default `gp2` type.
- The DevOps team manually identifies the non-compliant volume and modifies it to `gp3`.
- This process is time-consuming and prone to human error.

### **After Automation**
- The developer creates an EBS volume.
- The CloudWatch Event Rule triggers the Lambda function.
- The Lambda function automatically converts the volume to `gp3` within seconds.
- No manual intervention is required, ensuring compliance and saving time.

---

## **Limitations**
- The script assumes that the event payload contains the `resources` key with the volume ARN. If the event structure changes, the script may need to be updated.
- The function only modifies newly created volumes. Existing non-compliant volumes must be handled separately.

---

## **Future Enhancements**
1. **Multi-Resource Support**:
   - Extend the solution to enforce compliance for other AWS resources, such as EC2 instances, S3 buckets, and RDS databases.

2. **Tagging Policies**:
   - Automatically apply tags to newly created volumes for better resource tracking and cost allocation.

3. **Notification System**:
   - Integrate with Amazon SNS to notify the DevOps team when a volume is modified.

---

## **Contributing**
Feel free to open issues or submit pull requests to improve the script or add new features.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

This documentation provides a clear explanation of the problem, solution, and deployment steps, making it easy for others to understand and use the project.
