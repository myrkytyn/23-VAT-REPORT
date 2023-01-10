import 'dart:io';

class RunExecutable {
  static runProgram(command) {
    Process.run(command, [], runInShell: true);
  }
}
