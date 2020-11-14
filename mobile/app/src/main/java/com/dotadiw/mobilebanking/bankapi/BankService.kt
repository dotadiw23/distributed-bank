package com.dotadiw.mobilebanking.bankapi


import com.dotadiw.mobilebanking.entities.Credentials
import retrofit2.Call
import retrofit2.http.Body
import retrofit2.http.POST

/*
 * Interface for the communication with the REST API
 */
interface BankService {

    /*
     * Send the account number and password to the API to authenticate the user
     * if the request is ok, the server returns the access token
     */
    @POST("login")
    fun getAccount(@Body credentials: Credentials): Call<String>

}