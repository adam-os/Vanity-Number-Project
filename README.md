# Vanity-Number-Project
This project entailed creating a Lambda function that converts phone numbers to vanity numbers and then saving them in a DynamoDB table. 
Then, a contract flow is formalised on Amazon connect.
In this documentation, I will frstly focus on the code, then the Lambda function and then the Amazon Connect.

Code:

The decision to go with a for loop was due to its simplicity. I was able to succcessfully convert each digit in a phone to a corresponding letter randomised letter.
Initially, I struggled getting the right concept for the code but I chose a simplistic loop due to ease and swift malleability of the code. 
If I had more time, I would:
1) Add iteration to code so as to produce a number of possibilities instantly for one number. That way, I could pick the best 5 vanity numbers.
2) Utilise an external dictionary of words which would narrow the randon fuction to pick from a list of possible outcoumes. 
   This is because the 'best' vanity numbers are those that are easy to remember and recall. 
3) Make use of more error handling. Although I did do some incremental small tests to ensure that my code was sound,
   more usage of error handling and troubleshooting would be necessary when dealing with a client's product.

Lambda Function:

I was able to run a complete function with the code written whilst also transferring the output 'VNumber' into a key/value DynamoDB table.
Furthermore, I established a connection between the function and my contract flow line number in Amazon Connect.
Initially, I was prevented from running the function due to access denial to DynamoDB. I had to access IAM and assign a DynamoDB role to the Lambda function.

Amazon Connect:

I managed to create a contract flow which relayed an automated voice message. It is supposed to relay the vanity number of the incoming caller (variable labelled "VNumber").
Number: +442080686657
If I had more time I would:
1) Incorporate a method of relaying the vanity number back to the caller.
2) Add some extra features to the contract flow to increase the complexity.
