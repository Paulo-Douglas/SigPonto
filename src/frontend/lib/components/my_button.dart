import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:google_fonts/google_fonts.dart';
import '../service/service.dart';

class MyButton extends HookWidget {
  final String actionButton;
  final ValueNotifier<String> user;

  const MyButton({super.key, required this.actionButton, required this.user});

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: () async => await Service(user: user.value).login(),
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
