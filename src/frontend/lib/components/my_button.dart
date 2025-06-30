import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import '../styles/button.dart';

class MyButton extends HookWidget {
  final String actionButton;
  final VoidCallback onPressed;
  final String styleButton;

  const MyButton({
    super.key,
    required this.actionButton,
    required this.onPressed,
    this.styleButton = "",
  });

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: onPressed,
      style: styleButton.isNotEmpty
          ? MyStyle.yellowButton
          : MyStyle.greenButton,
      child: Text(actionButton, style: Theme.of(context).textTheme.labelLarge),
    );
  }
}
