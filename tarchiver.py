import os
import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
import argparse

console = Console()

class TArchiver:
    def __init__(self):
        self.console = console

    def create_zip(self, archive_name, files):
        command = ['zip', '-r', archive_name] + files
        self._run_command(command, f"Created ZIP archive: {archive_name}")

    def extract_zip(self, archive_name, destination):
        command = ['unzip', archive_name, '-d', destination]
        self._run_command(command, f"Extracted ZIP archive: {archive_name}")

    def create_tar(self, archive_name, files):
        command = ['tar', '-cvf', archive_name] + files
        self._run_command(command, f"Created TAR archive: {archive_name}")

    def extract_tar(self, archive_name, destination):
        command = ['tar', '-xvf', archive_name, '-C', destination]
        self._run_command(command, f"Extracted TAR archive: {archive_name}")

    def create_tar_gz(self, archive_name, files):
        command = ['tar', '-czvf', archive_name] + files
        self._run_command(command, f"Created TAR.GZ archive: {archive_name}")

    def extract_tar_gz(self, archive_name, destination):
        command = ['tar', '-xzvf', archive_name, '-C', destination]
        self._run_command(command, f"Extracted TAR.GZ archive: {archive_name}")

    def create_gzip(self, archive_name, file):
        command = ['gzip', '-k', file]
        self._run_command(command, f"Created GZIP archive: {archive_name}")

    def gunzip(self, archive_name, destination):
        command = ['gunzip', '-c', archive_name]
        self._run_command(command, f"Gunzip extraction: {archive_name}", destination)

    def create_7z(self, archive_name, files, password=None):
        command = ['7z', 'a', archive_name] + files
        if password:
            command.insert(2, f'-p{password}')
        self._run_command(command, f"Created 7z archive: {archive_name}")

    def extract_7z(self, archive_name, destination, password=None):
        command = ['7z', 'x', archive_name, f'-o{destination}']
        if password:
            command.insert(2, f'-p{password}')
        self._run_command(command, f"Extracted 7z archive: {archive_name}")

    def create_rar(self, archive_name, files, password=None):
        command = ['rar', 'a', archive_name] + files
        if password:
            command.insert(2, f'-p{password}')
        self._run_command(command, f"Created RAR archive: {archive_name}")

    def extract_rar(self, archive_name, destination, password=None):
        command = ['unrar', 'x', archive_name, f'{destination}/']
        if password:
            command.insert(2, f'-p{password}')
        self._run_command(command, f"Extracted RAR archive: {archive_name}")

    def extract_xz(self, archive_name, destination):
        command = ['xz', '-d', archive_name]
        self._run_command(command, f"Extracted XZ archive: {archive_name}")

    def list_files(self, archive_name):
        if archive_name.endswith('.zip'):
            command = ['unzip', '-l', archive_name]
        elif archive_name.endswith('.tar') or archive_name.endswith('.tar.gz'):
            command = ['tar', '-tvf', archive_name]
        elif archive_name.endswith('.7z'):
            command = ['7z', 'l', archive_name]
        elif archive_name.endswith('.rar'):
            command = ['unrar', 'l', archive_name]
        elif archive_name.endswith('.xz'):
            console.print(Panel(f"Listing files in XZ archive: {archive_name} is not supported.", style="red"))
            return
        else:
            console.print(Panel(f"Unsupported archive format for listing: {archive_name}", style="red"))
            return

        self._run_command(command, f"Listing files in {archive_name}")

    def _run_command(self, command, success_msg, destination=None):
        try:
            subprocess.run(command, check=True)
            if destination:
                with open(destination, 'wb') as out_file:
                    subprocess.run(command, stdout=out_file)
            self.console.print(Panel(success_msg, style="green"))
        except subprocess.CalledProcessError as e:
            self.console.print(Panel(f"Error: {e}", style="red"))

    def validate_path(self, path):
        if not os.path.exists(path):
            self.console.print(Panel(f"Error: {path} does not exist", style="red"))
            return False
        return True

def main():
    parser = argparse.ArgumentParser(description="TArchiver - Advanced Archiving Tool")
    parser.add_argument("command", choices=['create', 'extract', 'list'], help="Command to execute")
    parser.add_argument("archive", help="Path to the archive file")
    parser.add_argument("files", nargs="*", help="Files to add to the archive or extract")
    parser.add_argument("-p", "--password", help="Password for encrypted archives")

    args = parser.parse_args()
    archiver = TArchiver()

    if args.command == 'create':
        if not args.files:
            archiver.console.print(Panel("Please provide files to create an archive", style="red"))
            return
        if args.archive.endswith('.zip'):
            archiver.create_zip(args.archive, args.files)
        elif args.archive.endswith('.tar'):
            archiver.create_tar(args.archive, args.files)
        elif args.archive.endswith('.tar.gz'):
            archiver.create_tar_gz(args.archive, args.files)
        elif args.archive.endswith('.gz'):
            archiver.create_gzip(args.archive, args.files[0])
        elif args.archive.endswith('.7z'):
            archiver.create_7z(args.archive, args.files, args.password)
        elif args.archive.endswith('.rar'):
            archiver.create_rar(args.archive, args.files, args.password)
        else:
            archiver.console.print(Panel(f"Unsupported archive type for creation: {args.archive}", style="red"))

    elif args.command == 'extract':
        if archiver.validate_path(args.archive):
            if args.archive.endswith('.zip'):
                archiver.extract_zip(args.archive, args.files[0])
            elif args.archive.endswith('.tar') or args.archive.endswith('.tar.gz'):
                archiver.extract_tar(args.archive, args.files[0])
            elif args.archive.endswith('.gz'):
                archiver.gunzip(args.archive, args.files[0])
            elif args.archive.endswith('.7z'):
                archiver.extract_7z(args.archive, args.files[0], args.password)
            elif args.archive.endswith('.rar'):
                archiver.extract_rar(args.archive, args.files[0], args.password)
            elif args.archive.endswith('.xz'):
                archiver.extract_xz(args.archive, args.files[0])
            else:
                archiver.console.print(Panel(f"Unsupported archive type for extraction: {args.archive}", style="red"))

    elif args.command == 'list':
        if archiver.validate_path(args.archive):
            archiver.list_files(args.archive)

if __name__ == "__main__":
    main()
