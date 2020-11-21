package com.dotadiw.mobilebanking.ui.recyclerview

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.dotadiw.mobilebanking.R
import com.dotadiw.mobilebanking.model.Transaction

class RecyclerAdapter(private val transactionsList: ArrayList<Transaction>): RecyclerView.Adapter<RecyclerAdapter.ViewHolder>( ) {

    private lateinit var viewHolder: ViewHolder

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.transaction_item_list, parent, false)
        viewHolder = ViewHolder(view)
        return viewHolder
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        val item = transactionsList.get(position)
        holder.transactionId.text = "Transaction no: ${item.transactionId}"
        holder.origin.text = "From: ${item.origin}"
        holder.destination.text = "To: ${item.destination}"
        holder.amount.text = "Amount: $${item.amount}"
        holder.transactionDate.text = item.transactionDate
    }

    override fun getItemCount(): Int = transactionsList.size

    inner class ViewHolder(view: View): RecyclerView.ViewHolder(view) {

        val transactionId: TextView = view.findViewById(R.id.transactionId)
        val origin: TextView = view.findViewById(R.id.transactionOrigin)
        val destination: TextView = view.findViewById(R.id.transactionDestination)
        val amount: TextView = view.findViewById(R.id.transactionAmount)
        val transactionDate: TextView = view.findViewById(R.id.transactionDate)

    }

}