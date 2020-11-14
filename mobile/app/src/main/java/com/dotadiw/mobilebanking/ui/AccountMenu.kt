package com.dotadiw.mobilebanking.ui

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.dotadiw.mobilebanking.R

class AccountMenu : AppCompatActivity() {

    var accessToken:String? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_account_menu)

        accessToken = intent.getStringExtra("accessToken")
        println(accessToken)

    }
}