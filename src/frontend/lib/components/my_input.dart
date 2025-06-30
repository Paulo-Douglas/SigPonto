import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';

class MyInput extends HookWidget {
  final String helpText;
  final String label;
  final IconData? icon;
  final ValueNotifier<String> user;
  final Function(String) login;

  const MyInput({
    super.key,
    required this.login,
    required this.user,
    this.helpText = "",
    this.label = "",
    this.icon,
  });
  @override
  Widget build(BuildContext context) {
    return TextField(
      onSubmitted: login,
      onChanged: (value) => user.value = value,
      style: Theme.of(context).textTheme.bodyLarge,
      decoration: InputDecoration(
        helperText: helpText,
        helperStyle: Theme.of(context).textTheme.labelSmall,
        labelText: label,
        labelStyle: Theme.of(context).textTheme.bodyLarge,
        prefixIcon: icon != null ? Icon(icon) : null,
        prefixIconColor: Theme.of(context).colorScheme.onPrimary,
        enabledBorder: OutlineInputBorder(
          borderSide: BorderSide(
            color: Theme.of(context).colorScheme.onPrimary,
          ),
        ),
        border: OutlineInputBorder(borderRadius: BorderRadius.circular(10)),
        focusedBorder: OutlineInputBorder(
          borderSide: BorderSide(
            color: Theme.of(context).colorScheme.onPrimary,
            width: 2,
          ),
        ),
        errorBorder: OutlineInputBorder(
          borderSide: BorderSide(
            color: Theme.of(context).colorScheme.error,
            width: 2,
          ),
        ),
      ),
    );
  }
}
