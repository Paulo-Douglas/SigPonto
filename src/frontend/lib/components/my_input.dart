import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:google_fonts/google_fonts.dart';

class MyInput extends HookWidget {
  final String helpText;
  final String label;
  final IconData? icon;

  const MyInput({super.key, this.helpText = "", this.label = "", this.icon});

  @override
  Widget build(BuildContext context) {
    return TextField(
      decoration: InputDecoration(
        helperText: helpText,
        helperStyle: TextStyle(
          fontFamily: GoogleFonts.alef().fontFamily,
          color: Colors.white70,
        ),
        labelText: label,
        labelStyle: TextStyle(
          fontFamily: GoogleFonts.alef().fontFamily,
          color: Colors.white70,
        ),
        prefixIcon: icon != null ? Icon(icon) : null,
        prefixIconColor: Colors.white70,
        enabledBorder: OutlineInputBorder(
          borderSide: BorderSide(color: Colors.white70),
        ),
        border: OutlineInputBorder(borderRadius: BorderRadius.circular(10)),
        focusedBorder: OutlineInputBorder(
          borderSide: BorderSide(color: Colors.white, width: 2),
        ),
        errorBorder: OutlineInputBorder(
          borderSide: BorderSide(color: Colors.redAccent, width: 2),
        ),
      ),
    );
  }
}
