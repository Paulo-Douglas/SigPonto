import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:google_fonts/google_fonts.dart';

class MyButton extends HookWidget {
  final String actionButton;
  final ValueNotifier<String> user;
  final ValueNotifier<String> tokenUser;
  final VoidCallback onPressed;

  const MyButton({
    super.key,
    required this.actionButton,
    required this.user,
    required this.tokenUser,
    required this.onPressed,
  });

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: onPressed,
      style: ButtonStyle(
        textStyle: WidgetStateProperty.resolveWith((states) {
          return TextStyle(
            fontFamily: GoogleFonts.alef().fontFamily,
            color: Colors.red,
            fontWeight: FontWeight.bold,
          );
        }),
        foregroundColor: WidgetStateProperty.resolveWith((states) {
          return Colors.red;
        }),
      ),
      child: Text(actionButton, style: TextStyle(color: Colors.blueGrey)),
    );
  }
}
