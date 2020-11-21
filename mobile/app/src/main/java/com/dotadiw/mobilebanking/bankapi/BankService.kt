package com.dotadiw.mobilebanking.bankapi


import com.dotadiw.mobilebanking.model.Account
import com.dotadiw.mobilebanking.model.Credentials
import com.dotadiw.mobilebanking.model.Transaction
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
     * if the request is ok, the server returns the access token
     */
    @GET("account/{token}")
    fun getAccount(@Path("token") token: String): Call<Account>

    /*
     *
     */
    @GET("transactions/{token}")
    fun getTransactionsHistory(@Path("token") token: String): Call<List<Transaction>>
}