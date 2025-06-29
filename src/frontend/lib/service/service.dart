class Service {
  String _user;

  Service({String user = ""}) : _user = user;

  // _login() {
  //   // ignore: avoid_print
  //   print(_user);
  // }

  String get user {
    // ignore: avoid_print
    print(_user);
    return _user;
  }
}
