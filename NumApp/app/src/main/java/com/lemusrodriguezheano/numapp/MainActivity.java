package com.lemusrodriguezheano.numapp;

import android.net.Uri;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v4.app.Fragment;
import android.view.View;
import android.support.design.widget.NavigationView;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;

import com.lemusrodriguezheano.numapp.oneVariable.busquedaIncremental;
import com.lemusrodriguezheano.numapp.oneVariable.bisection;
import com.lemusrodriguezheano.numapp.oneVariable.falsePosition;
import com.lemusrodriguezheano.numapp.oneVariable.fixedPoint;
import com.lemusrodriguezheano.numapp.oneVariable.newton;
import com.lemusrodriguezheano.numapp.oneVariable.secant;
import com.lemusrodriguezheano.numapp.oneVariable.multipleRoots;

public class MainActivity extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener,
            busquedaIncremental.OnFragmentInteractionListener,
            bisection.OnFragmentInteractionListener,
            falsePosition.OnFragmentInteractionListener,
            fixedPoint.OnFragmentInteractionListener,
            newton.OnFragmentInteractionListener,
            secant.OnFragmentInteractionListener,
            multipleRoots.OnFragmentInteractionListener {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        /**
        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });
        **/
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.addDrawerListener(toggle);
        toggle.syncState();

        NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
        navigationView.setNavigationItemSelectedListener(this);
    }

    @Override
    public void onBackPressed() {
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();
        Fragment fragment = null;
        Boolean fragmentoSeleccionado = false;




        if (id == R.id.btn_incrementalSearch) {
            fragment = new busquedaIncremental();
            //getSupportFragmentManager().beginTransaction().replace(R.id.Contenedor, fragment).commit();
            fragmentoSeleccionado = true;

        } else if (id == R.id.btn_bisection) {
            fragment = new bisection();
            fragmentoSeleccionado = true;

        } else if (id == R.id.btn_falsePosition) {
            fragment = new falsePosition();
            fragmentoSeleccionado = true;

        } else if (id == R.id.btn_fixedPoint) {
            fragment = new fixedPoint();
            fragmentoSeleccionado = true;

        } else if (id == R.id.btn_newton) {
            fragment = new newton();
            fragmentoSeleccionado = true;
        } else if (id == R.id.btn_secant) {
            fragment = new secant();
            fragmentoSeleccionado = true;
        } else if (id == R.id.btn_multipleRoots) {
            fragment = new multipleRoots();
            fragmentoSeleccionado = true;
        } else if (id == R.id.btn_home) {
            fragment = new home();
            fragmentoSeleccionado = true;
        }
/**
        } else if (id == R.id.nav_share) {

        } else if (id == R.id.nav_send) {

        }
**/

        if (fragmentoSeleccionado){
            getSupportFragmentManager().beginTransaction().replace(R.id.Contenedor, fragment).commit();
        }
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }

    @Override
    public void onFragmentInteraction(Uri uri) {

    }
}