package com.glebrasskazov.gRGBc;
import android.app.Activity;
import android.os.Bundle;
import android.text.Editable;
import android.text.InputFilter;
import android.text.TextWatcher;
import android.widget.EditText;
import android.widget.TextView;
import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;
public class MainActivity extends Activity {
    Python python;
    PyObject pyObject;
    int r=0, g=0, b=0;
    TextView textView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        if (! Python.isStarted()) {
            Python.start(new AndroidPlatform(this));
        }
        python=Python.getInstance();
        pyObject=python.getModule("script1");
        textView=findViewById(R.id.textV);
        final EditText rEdit, gEdit, bEdit;
        rEdit=findViewById(R.id.rE);
        gEdit=findViewById(R.id.gE);
        bEdit=findViewById(R.id.bE);
        TextWatcher watcher=new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }
            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {

            }
            @Override
            public void afterTextChanged(Editable s) {
                if(!rEdit.getText().toString().equals(""))r=Integer.parseInt(rEdit.getText().toString());
                if(!gEdit.getText().toString().equals(""))g=Integer.parseInt(gEdit.getText().toString());
                if(!bEdit.getText().toString().equals(""))b=Integer.parseInt(bEdit.getText().toString());
                textView.setText(pyObject.callAttr("predictColor", r, g, b).toString());
            }
        };
        rEdit.setFilters(new InputFilter[]{ new com.glebrasskazov.scickit_android.InputFilterMinMax("0", "255")});
        gEdit.setFilters(new InputFilter[]{ new com.glebrasskazov.scickit_android.InputFilterMinMax("0", "255")});
        bEdit.setFilters(new InputFilter[]{ new com.glebrasskazov.scickit_android.InputFilterMinMax("0", "255")});
        rEdit.addTextChangedListener(watcher);
        gEdit.addTextChangedListener(watcher);
        bEdit.addTextChangedListener(watcher);
        textView.setText(pyObject.callAttr("predictColor", r, g, b).toString());
    }
}
