package com.dotadiw.mobilebanking.ui.fragments

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.core.os.bundleOf
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.dotadiw.mobilebanking.R
import com.dotadiw.mobilebanking.model.Transaction
import com.dotadiw.mobilebanking.ui.recyclerview.RecyclerAdapter


class TransactionsFragment : Fragment() {

    private var transactionList: ArrayList<String>? = null
    private lateinit var recyclerView: RecyclerView
    private lateinit var viewAdapter: RecyclerAdapter
    private lateinit var layoutManager: RecyclerView.LayoutManager

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        transactionList = this.arguments?.getStringArrayList("transactions")
        println(transactionList)
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        val view = inflater.inflate(R.layout.fragment_transactions, container, false)

        // Setup RecyclerView
        val list: ArrayList<Transaction> = ArrayList()
        for (transaction in transactionList!!) {
            val transactionArray = transaction.split("&")
            println(transactionArray[0])
            println(transactionArray[1])
            println(transactionArray[2])
            println(transactionArray[3])
            println(transactionArray[4])
            list.add(Transaction(transactionArray[0].toInt(), transactionArray[1], transactionArray[2], transactionArray[3].toFloat(), transactionArray[4]))
        }

        recyclerView = view.findViewById(R.id.transaction_recycler_view)
        layoutManager = LinearLayoutManager(activity)
        viewAdapter = RecyclerAdapter(list)
        recyclerView.layoutManager = layoutManager
        recyclerView.adapter = viewAdapter

        return view
    }

    private fun setupRecyclerView() {
        recyclerView.layoutManager = LinearLayoutManager(activity)
    }

}