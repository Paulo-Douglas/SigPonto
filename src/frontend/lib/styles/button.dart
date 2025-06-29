import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class MyStyle {
  // Estilo de botão verde
  static ButtonStyle greenButton = ElevatedButton.styleFrom(
    backgroundColor: Color.fromARGB(255, 10, 200, 100), // Verde suave
    foregroundColor: Colors.white, // Texto branco
    padding: EdgeInsets.symmetric(horizontal: 24, vertical: 12),
    textStyle: GoogleFonts.poppins(fontSize: 16, fontWeight: FontWeight.w600),
    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
  );

  // Estilo de botão amarelo
  static ButtonStyle yellowButton = ElevatedButton.styleFrom(
    backgroundColor: Colors.lightBlueAccent.withValues(
      blue: 10,
    ), // Amarelo forte
    foregroundColor: Colors.black87, // Contraste escuro no texto
    padding: EdgeInsets.symmetric(horizontal: 24, vertical: 12),
    textStyle: GoogleFonts.poppins(fontSize: 16, fontWeight: FontWeight.w600),
    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
  );
}
