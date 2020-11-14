package com.dotadiw.mobilebanking.ui

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.dotadiw.mobilebanking.R
import com.dotadiw.mobilebanking.bankapi.BankService
import com.dotadiw.mobilebanking.entities.Credentials
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class MainActivity : AppCompatActivity() {

    private val HOST = "192.168.0.3"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Login views
        val accountInput: EditText = findViewById(R.id.accountNoInput)
        val passwordInput: EditText = findViewById(R.id.passwordInput)

        val button: Button = findViewById(R.id.button)
        button.setOnClickListener {
            login(accountInput.text.toString(), passwordInput.text.toString())
        }

    }

    /*
     * login() allows to the app make a HTTP request to the API and get an access
     * token if the sent credentials are valid
     */
    private fun login(accountNo: String, password: String) {
        if (accountNo.isNotEmpty() && password.isNotEmpty()) {
            val retrofit = restEngine() // Instance retrofit

            val apiService: BankService = retrofit.create(BankService::class.java)
            val res: Call<String> = apiService.getAccount(Credentials(accountNo, password))

            res.enqueue(object : Callback<String> {
                override fun onResponse(call: Call<String>, response: Response<String>) {
                    val accessToken = response.body().toString()

                    if (accessToken == "Account not found") Toast.makeText(
                        this@MainActivity, R.string.no_account, Toast.LENGTH_SHORT
                    ).show()
                    else {
                        // Start a new activity and send the access token
                        val intent = Intent(this@MainActivity, AccountMenu::class.java)
                        intent.putExtra("accessToken", accessToken)
                        startActivity(intent)
                    }
                }

                override fun onFailure(call: Call<String>, t: Throwable) {
                    println("Something is wrong!")
                }
            })
        } else Toast.makeText(this, R.string.empty_fields, Toast.LENGTH_SHORT).show()
    }

    /*
     * Retrofit configuration to make HTTP request
     */
    private fun restEngine(): Retrofit {

        return Retrofit.Builder()
            .baseUrl("http://$HOST:5000/")
            .addConverterFactory(GsonConverterFactory.create())
            .build()
    }
}