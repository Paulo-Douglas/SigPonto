import 'package:flutter/material.dart';
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
  textTheme: const TextTheme(
    bodyLarge: TextStyle(color: Colors.black87),
    bodyMedium: TextStyle(color: Colors.black54),
    titleLarge: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
  ),
);
