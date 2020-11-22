package com.dotadiw.mobilebanking.ui.fragments

import android.content.Context
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import com.dotadiw.mobilebanking.R
import com.dotadiw.mobilebanking.interfaces.OnDataPass
import com.dotadiw.mobilebanking.ui.AccountMenu


class TransferFragment : Fragment() {

    private var accessToken: String? = null
    private lateinit var passData: OnDataPass

    private lateinit var destinationTxt: TextView
    private lateinit var amountTxt: TextView
    private lateinit var submitBtn: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        accessToken = this.arguments?.getString("token")
    }

    override fun onAttach(context: Context) {
        super.onAttach(context)
        passData = context as OnDataPass
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        val view = inflater.inflate(R.layout.fragment_transafer, container, false)

        destinationTxt = view.findViewById(R.id.transferDestinationInput)
        amountTxt = view.findViewById(R.id.transferAmountInput)
        submitBtn = view.findViewById(R.id.makeTransferBtn)

        submitBtn.setOnClickListener {
            sendToActivity()
        }

        return view
    }

    private fun sendToActivity() {
        val destination = destinationTxt.text.toString()
        val amount = amountTxt.text.toString()

        if (destination.isEmpty() || amount.isEmpty()) {
            Toast.makeText(activity, R.string.empty_fields, Toast.LENGTH_SHORT).show()
        }else {
            passData.onDataPass(arrayOf(destination, amount))
        }
    }

}