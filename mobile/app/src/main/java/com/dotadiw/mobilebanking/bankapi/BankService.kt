package com.dotadiw.mobilebanking.bankapi


import com.dotadiw.mobilebanking.model.Account
import com.dotadiw.mobilebanking.model.Credentials
import com.dotadiw.mobilebanking.model.Transaction
import com.dotadiw.mobilebanking.model.TransferData
import retrofit2.Call
import retrofit2.http.*

/*
 * Interface for the communication with the REST API
 */
interface BankService {

    /*
     * Send the account number and password to the API to authenticate the user
     * if the request is ok, the server returns the access token
     */
    @POST("login")
    fun login(@Body credentials: Credentials): Call<String>

    /*
     * According to the user token the API returns a list of the
     * account information
     */
    @GET("account/{token}")
    fun getAccount(@Path("token") token: String): Call<Account>

    /*
     * According to the user token the API returns a list of the
     * account transactions
     */
    @GET("transactions/{token}")
    fun getTransactionsHistory(@Path("token") token: String): Call<List<Transaction>>

    /*
     * According to the situation the server can response
     * 5 -> If the account does not have enough money
     * 4 -> The destination account does not exists
     * 3 -> If a database error has occurred
     * 2 -> If the request is not valid1 -> If the transaction is successful
     * 0 -> The transaction has failed
     */
    @POST("transactions/{token}")
    fun makeTransfer(@Path("token") token: String, @Body transferData: TransferData): Call<Int>

}