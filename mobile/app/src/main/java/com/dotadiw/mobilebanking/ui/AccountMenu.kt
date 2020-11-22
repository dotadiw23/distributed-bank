package com.dotadiw.mobilebanking.ui

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import androidx.fragment.app.Fragment
import androidx.fragment.app.FragmentTransaction
import com.dotadiw.mobilebanking.R
import com.dotadiw.mobilebanking.bankapi.BankService
import com.dotadiw.mobilebanking.interfaces.OnDataPass
import com.dotadiw.mobilebanking.model.Account
import com.dotadiw.mobilebanking.model.Transaction
import com.dotadiw.mobilebanking.model.TransferData
import com.dotadiw.mobilebanking.ui.fragments.AccountFragment
import com.dotadiw.mobilebanking.ui.fragments.TransactionsFragment
import com.dotadiw.mobilebanking.ui.fragments.TransferFragment
import com.google.android.material.bottomnavigation.BottomNavigationView
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class AccountMenu : AppCompatActivity(), OnDataPass {

    private lateinit var accessToken: String
    private val bundle = Bundle()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_account_menu)

        // Validate the token that sent main activity
        if (intent.getStringExtra("accessToken") != null) {
            accessToken = intent.getStringExtra("accessToken").toString()
        } else {
            finish()
        }

        val bottomNavigationView: BottomNavigationView = findViewById(R.id.bottomNavigation)
        bottomNavigationView.setOnNavigationItemSelectedListener { item ->
            when (item.itemId) {
                R.id.account -> getAccountInfo(accessToken)
                R.id.money_transfer -> showFragment(TransferFragment())
                R.id.transaction_history -> getTransactionHistory(accessToken)
            }

            true
        }
    }

    /*
     * Interface to pass data between the fragment transfer form
     * and the container activity
     */
    override fun onDataPass(data: Array<String>) {
        val retrofit = restEngine()

        val apiService: BankService = retrofit.create(BankService::class.java)
        val res: Call<Int> = apiService.makeTransfer(accessToken, TransferData(data[0], data[1].toFloat()))

        res.enqueue(object : Callback<Int> {

            override fun onResponse(call: Call<Int>, response: Response<Int>) {

                when (response.body()) {
                    5 -> Toast.makeText(this@AccountMenu, R.string.no_money, Toast.LENGTH_SHORT).show()
                    4 -> Toast.makeText(this@AccountMenu, R.string.no_destination, Toast.LENGTH_SHORT).show()
                    3 -> Toast.makeText(this@AccountMenu, R.string.database_err, Toast.LENGTH_SHORT).show()
                    2 -> Toast.makeText(this@AccountMenu, R.string.invalid_request, Toast.LENGTH_SHORT).show()
                    1 -> Toast.makeText(this@AccountMenu, R.string.transfer_successful, Toast.LENGTH_SHORT).show()
                }
                
            }

            override fun onFailure(call: Call<Int>, t: Throwable) {
                println("Something is wrong!")
            }
        })
    }


    /*
     * getTransactionHistory() allows to the app make a HTTP request to the API and get a list
     * of all transactions associated with the account
     */
    private fun getTransactionHistory(accessToken: String) {
        val retrofit = restEngine()

        val apiService: BankService = retrofit.create(BankService::class.java)
        val res: Call<List<Transaction>> = apiService.getTransactionsHistory(accessToken)

        res.enqueue(object : Callback<List<Transaction>> {
            override fun onResponse(
                call: Call<List<Transaction>>,
                response: Response<List<Transaction>>
            ) {
                val transactionList = response.body()

                if (transactionList != null) {
                    val bundleList = ArrayList<String>()
                    for (transaction in transactionList) {
                        bundleList.add("${transaction.transactionId}&${transaction.origin}&${transaction.destination}&${transaction.amount}&${transaction.transactionDate}")
                    }
                    bundle.putStringArrayList("transactions", bundleList)
                    showFragment(TransactionsFragment())
                }
            }

            override fun onFailure(call: Call<List<Transaction>>, t: Throwable) {
                print("Something is wrong!")
            }
        })
    }

    /*
     * getAccountInfo() allows to the app make a HTTP request to the API and get account
     * data based in the sent access token
     */
    private fun getAccountInfo(accessToken: String) {
        val retrofit = restEngine()

        val apiService: BankService = retrofit.create(BankService::class.java)
        val res: Call<Account> = apiService.getAccount(accessToken)

        res.enqueue(object : Callback<Account> {
            override fun onResponse(call: Call<Account>, response: Response<Account>) {
                val account = response.body()
                println(response.body())
                if (account != null) {
                    val data = arrayListOf(
                        account.accountNo,
                        account.owner,
                        account.amount.toString(),
                        account.createdAt
                    )
                    bundle.putStringArrayList("data", data)
                    showFragment(AccountFragment())
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
            .baseUrl("http://192.168.0.8:5000/")
            .addConverterFactory(GsonConverterFactory.create())
            .build()
    }

    /*
     * Make the fragment transaction
     */
    private fun showFragment(fragment: Fragment) {
        val fragmentManager = supportFragmentManager
        val fragmentTransaction = fragmentManager.beginTransaction()
        fragment.arguments = bundle
        fragmentTransaction.replace(R.id.fragment_container, fragment).commit()

    }

}