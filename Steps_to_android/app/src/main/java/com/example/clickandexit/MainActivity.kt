package com.example.clickandexit

import android.os.Bundle
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Arrangement

import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import com.example.clickandexit.ui.theme.ClickandexitTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            ClickandexitTheme {
                Column(
                    modifier = Modifier.fillMaxWidth().padding(vertical = 400.dp),
                    verticalArrangement = Arrangement.Center,
                    horizontalAlignment = Alignment.CenterHorizontally,
                ) {
                val context = LocalContext.current
                    Button(
                        onClick = {
                        /*    Toast.makeText(
                                context,
                                "Exiting...",
                                Toast.LENGTH_LONG)
                                .show() */
                            finish();
                            System.exit(0);
                        }
                    ) {
                        Text(text = "Click and Exit")
                    }
                }
            }
        }
    }
}