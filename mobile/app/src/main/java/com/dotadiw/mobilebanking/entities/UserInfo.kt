package com.dotadiw.mobilebanking.entities

import com.google.gson.annotations.SerializedName

/*
 * Set of data class that allows the JSON parse of the different
 * API server responses
 */

data class Account (
    @SerializedName("account_no")
    val accountNo: String,
    val amount: Int,
    val owner: String,
    @SerializedName("created_at")
    val createdAt: String
)

data class Credentials (
    @SerializedName("account_no")
    val accountNo: String,
    val password: String
)
