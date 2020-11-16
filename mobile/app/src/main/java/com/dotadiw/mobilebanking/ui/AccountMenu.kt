package com.dotadiw.mobilebanking.ui

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.fragment.app.Fragment
import androidx.fragment.app.FragmentTransaction
import com.dotadiw.mobilebanking.R
import com.dotadiw.mobilebanking.bankapi.BankService
import com.dotadiw.mobilebanking.entities.Account
import com.dotadiw.mobilebanking.ui.fragments.AccountFragment
import com.google.android.material.bottomnavigation.BottomNavigationView
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class AccountMenu : AppCompatActivity() {

    var accessToken: String? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_account_menu)

        accessToken = intent.getStringExtra("accessToken")

        //showFragment(AccountFragment(), "")

        val bottomNavigationView: BottomNavigationView = findViewById(R.id.bottomNavigation)
        bottomNavigationView.setOnNavigationItemSelectedListener { item ->
            when (item.itemId) {
                R.id.account -> {
                    getAccountInfo(accessToken!!)
                }
                //R.id.money_transfer -> showFragment(TransferFragment(), )
                //R.id.transaction_history -> showFragment(TransactionsFragment(), )
            }

            true
        }
    }

    // Make the fragment transaction
    private fun showFragment(fragment: Fragment, data: ArrayList<String>) {
        val fragmentManager = supportFragmentManager
        val fragmentTransaction = fragmentManager.beginTransaction()
        val bundle = Bundle()
        bundle.putStringArrayList("data", data)
        fragment.arguments = bundle
        fragmentTransaction.replace(R.id.fragment_container, fragment)
            .setTransition(FragmentTransaction.TRANSIT_FRAGMENT_FADE).commit()

    }

    /*
     * getAccount() allows to the app make a HTTP request to the API and get account
     * data based in the sent access token
     */
    private fun getAccountInfo(accessToken: String) {
        val retrofit = restEngine()

        val apiService: BankService = retrofit.create(BankService::class.java)
        val res: Call<Account> = apiService.getAccount(accessToken)

        res.enqueue(object : Callback<Account> {
            override fun onResponse(call: Call<Account>, response: Response<Account>) {
                val account = response.body()

                if (account != null) {
                    showFragment(AccountFragment(), arrayListOf(
                        account.accountNo,
                        account.owner,
                        account.amount.toString(),
                        account.createdAt
                    ))
                }
            }

            override fun onFailure(call: Call<Account>, t: Throwable) {
                print("Something is wrong!")
            }
        })
    }

    /*
     * Retrofit configuration to make HTTP request
     */
    private fun restEngine(): Retrofit {

        return Retrofit.Builder()
            .baseUrl("http://192.168.0.3:5000/")
            .addConverterFactory(GsonConverterFactory.create())
            .build()
    }
}