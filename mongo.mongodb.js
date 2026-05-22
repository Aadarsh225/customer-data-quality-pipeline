use("CustomerDB")

// Finding all the transaction in the data base
// db.transactions.find()

// Finding the transaction with fraud flag is true
// db.transactions.find({fraud_flag:true})

// Finding the transaction with invalid Phone number
// db.transactions.find({valid_phone:false})

// Finding the transaction with invalid email address
// db.transactions.find({valid_email:false})

// Finding the total number of transaction based on the payment method
// db.transactions.aggregate([
//     {
//         $group:{
//             _id:"$payment_method",
//             totaltransaction:{$sum:1}
//         }
//     }
// ])

// Finding the total amount based on the payment method
// db.transactions.aggregate([
//     {
//         $group:{
//             _id:"$payment_method",
//             totalamount:{$sum:"$amount"}
//         }
//     }
// ])

// finding total number of sucess transaction and failed transaction
// db.transactions.aggregate([
//     {
//         $group:{
//             _id:"$transaction_status",
//             totaltransaction:{$sum:1}
//         }
//     }
// ])

// finding the transaction amount on the basis of transaction status
// db.transactions.aggregate([
//     {
//         $group:{
//             _id:"$transaction_status",
//             totalamount:{$sum:"$amount"}
//         }
//     }
// ])

// Finding the total no of transaction based on location

// db.transactions.aggregate([
//     {
//         $group:{
//             _id:"$city",
//             totaltransaction:{$sum:1}
//         }
//     }
// ])

// Finding the totalamount on the basis of city

// db.transactions.aggregate([
//     {
//         $group:{
//             _id:"$city",
//             totalamount:{$sum:"$amount"}
//         }
//     }
// ])

// db.transactions.find({city:"Unknown"})


// Finding the total number of transaction on the basis of device_type
// db.transactions.aggregate([
//     {
//         $group:{
//             _id:"$device_type",
//             totaltransaction:{$sum:1}
//         }
//     }
// ])

// Finding the totalamount on the basis of the device_type
// db.transactions.aggregate([
//     {
//         $group:{
//             _id:"$device_type",
//             totalamount:{$sum:"$amount"}
//         }
//     }
// ])

// finding the fraud_flag transaction
// db.transactions.aggregate([
//     {
//         $match:{
//             fraud_flag:true
//         }
//     },{
//         $group:{
//             _id:"$fraud_flag",
//             totaltransaction:{$sum:1}
//         }
//     }
// ])

// finding the fraud_flag transaction amount
db.transactions.aggregate([
    {
        $match:{
            fraud_flag:true,

        }
    },
    {
        $group:{
            _id:"$fraud_flag",
            totalamount:{$sum:"$amount"}
        }
    }
])