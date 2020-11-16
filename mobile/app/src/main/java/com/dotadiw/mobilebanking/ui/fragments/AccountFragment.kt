package com.dotadiw.mobilebanking.ui.fragments

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import com.dotadiw.mobilebanking.R


class AccountFragment : Fragment() {

    private var accountInfo: ArrayList<String>? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        accountInfo = this.arguments?.getStringArrayList("data")
        print(accountInfo)
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        val view = inflater.inflate(R.layout.fragment_account, container, false)

        val welcomeText: TextView = view!!.findViewById(R.id.welcomeUserTxt)
        welcomeText.text = "Welcome ${accountInfo?.get(1)}"

        val accountNoText: TextView = view!!.findViewById(R.id.accountNumberTxt)
        accountNoText.text = "Account number: ${accountInfo?.get(0)}"

        val amountText: TextView = view!!.findViewById(R.id.amountTxt)
        amountText.text = "$ ${accountInfo?.get(2)}"

        val createdAtTxt: TextView = view!!.findViewById(R.id.createdAtTxt)
        createdAtTxt.text = "Account created at: ${accountInfo?.get(3)}"

        return view
    }


}