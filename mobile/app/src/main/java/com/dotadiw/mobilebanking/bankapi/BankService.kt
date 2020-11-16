package com.dotadiw.mobilebanking.bankapi


import com.dotadiw.mobilebanking.entities.Account
import com.dotadiw.mobilebanking.entities.Credentials
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

    @GET("account/{token}")
    fun getAccount(@Path("token") token: String): Call<Account>

}