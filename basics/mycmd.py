from __future__ import print_function
import cmd

class mycmd(cmd.Cmd):
      prompt = 'project >>> '
      intro = 'Initial deploy, kill, benchmark, report command prep.'

      def do_deploy(self, line):
          print('deploy')
      def do_kill(self, line):
          print('kill')
      def do_benchmark(self, line):
          print('benchmark')
      def do_report(self, line):
          print('report')

      def do_EOF(self, line):
          print('bye,bye')
          return True

if __name__ == '__main__':
      mycmd().cmdloop()
