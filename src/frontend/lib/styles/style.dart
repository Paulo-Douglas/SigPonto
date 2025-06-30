import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import './colors.dart';

final ThemeData customTheme = ThemeData(
  primaryColor: GetColor.blue.color,
  scaffoldBackgroundColor: GetColor.background.color,
  appBarTheme: AppBarTheme(
    backgroundColor: GetColor.blueLigth.color,
    foregroundColor: GetColor.white.color,
    elevation: 0,
  ),
  floatingActionButtonTheme: FloatingActionButtonThemeData(
    backgroundColor: GetColor.green.color,
    foregroundColor: GetColor.white.color,
  ),
  colorScheme: ColorScheme(
    primary: GetColor.blue.color,
    secondary: GetColor.greeSuav.color,
    surface: GetColor.greeLight.color,
    error: GetColor.red.color,
    onPrimary: GetColor.white.color,
    onSecondary: GetColor.white.color,
    onSurface: GetColor.blue.color,
    onError: GetColor.white.color,
    brightness: Brightness.light,
  ),
  textTheme: TextTheme(
    bodyLarge: TextStyle(
      color: Colors.black87,
      fontFamily: GoogleFonts.poppins().fontFamily,
    ),
    bodyMedium: TextStyle(
      color: GetColor.blue.color,
      fontSize: 12,
      fontWeight: FontWeight.w300,
      fontFamily: GoogleFonts.poppins().fontFamily,
    ),
    bodySmall: TextStyle(
      color: GetColor.blue.color,
      fontSize: 10,
      fontWeight: FontWeight.w300,
      fontFamily: GoogleFonts.poppins().fontFamily,
    ),
    labelSmall: TextStyle(
      color: const Color.fromARGB(221, 0, 0, 0),
      fontFamily: GoogleFonts.poppins().fontFamily,
      fontSize: 10,
      fontWeight: FontWeight.w600,
    ),
    labelLarge: TextStyle(
      color: Colors.white,
      fontFamily: GoogleFonts.poppins().fontFamily,
      fontSize: 15,
      fontWeight: FontWeight.bold,
    ),
    titleLarge: TextStyle(
      fontSize: 20,
      fontWeight: FontWeight.bold,
      fontFamily: GoogleFonts.poppins().fontFamily,
    ),
    titleMedium: TextStyle(
      fontSize: 18,
      fontFamily: GoogleFonts.poppins().fontFamily,
      fontWeight: FontWeight.bold,
      color: GetColor.blue.color,
    ),
  ),
);
