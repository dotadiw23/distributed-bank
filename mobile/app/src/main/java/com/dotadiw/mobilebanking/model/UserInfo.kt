package com.dotadiw.mobilebanking.model

import com.google.gson.annotations.SerializedName

/*
 * Set of data class that allows the JSON parse of the different
 * API server responses
 */

data class Account (
    @SerializedName("account_no")
    val accountNo: String,
    val amount: Int,
    @SerializedName("created_at")
    val createdAt: String,
    val owner: String
)

data class Credentials (
    @SerializedName("account_no")
    val accountNo: String,
    val password: String
)

data class Transaction(
    @SerializedName("transaction_id")
    val transactionId: Int,
    val origin: String,
    val destination: String,
    val amount: Float,
    @SerializedName("transaction_date")
    val transactionDate: String
)
