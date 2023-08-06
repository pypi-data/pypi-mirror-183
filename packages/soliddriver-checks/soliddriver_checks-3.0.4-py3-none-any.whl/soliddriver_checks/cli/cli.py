import click
import json
from ..api import analysis
from .terminal_logs import KMPTerminalOutput
from ..api.utils.remote_analysis import check_remote_servers
from .kmp_report import KMPReporter
from .km_report import KMReporter
import os
import logging
import socket
from pathlib import Path
from rich.logging import RichHandler
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from ..version import __VERSION__


FORMAT_TYPES = {
    "html": ".html",
    "xlsx": ".xlsx",
    "pdf": ".pdf",
    "json": ".json",
}


class Check_Target:
    def __init__(self, target):
        if target is None:
            target = "system"

        self.target = Path(target)

    @property
    def system(self):
        return self.target.name == "system" and not (
            self.target.is_file() or self.target.is_dir()
        )

    @property
    def rpm(self):
        # need better check than this
        if self.target.is_file() and self.target.name.endswith(".rpm"):
            return self.target
        return None

    @property
    def dir(self):
        if self.target.is_dir():
            return self.target
        return None

    @property
    def config(self):
        try:
            with self.target.open() as f:
                return json.load(f)
        except Exception as e:
            raise (e)


def with_format_suffix(path, format_type):
    suffix = FORMAT_TYPES.get(format_type, None)

    if suffix is None:
        return path

    if path.suffix == suffix:
        return path

    return path.parent / (path.name + suffix)


def export(exporter, check_result, out_format, dst):
    dst = with_format_suffix(dst, out_format)
    if out_format == "html":
        exporter.to_html(check_result, dst)
    elif out_format == "xlsx":
        exporter.to_xlsx(check_result, dst)
    elif out_format == "json":
        exporter.to_json(check_result, dst)


def dst_is_ok(dst, out_format):
    def check(dst):
        if dst.is_file():
            if not os.access(dst, os.W_OK):
                raise Exception("Cannot write to %s" % dst)
            return click.confirm("Overwrite %s?" % dst)
        return True

    if out_format == "all":
        for format_type, ext in FORMAT_TYPES.items():
            if ext is None:
                continue
            dst = dst.parent / (dst.name + ext)
            if not check(dst):
                return False
        return True

    else:
        ext = FORMAT_TYPES[out_format]
        dst = dst.parent / (dst.name + ext)
        return check(dst)


@click.command()
@click.argument("check_target", default="system")
@click.option(
    "--format",
    "-f",
    "out_format",
    type=click.Choice(FORMAT_TYPES),
    default="json",
    help="Specify output format (PDF is in Beta)",
)
@click.option(
    "--output",
    "-o",
    default=".",
    help="Output destination. Target can be filename or point "
    "existing directory "
    "If directory, files will be placed in the directory "
    "using a autmatically generated filename. If target "
    "is not an existing directory, file name is assumed "
    "and output files will use the path and file name "
    "specified. In either case, the file extension will "
    "be automatically appended matching on the output format",
)
@click.option("--version", is_flag=True)
def run(check_target, output, out_format, version):
    """Run checks against CHECK_TARGET.

    \b
    CHECK_TARGET can be:
      KMP file
      directory containing KMP files
      "system" to check locally installed kernel modules
      a config file listing remote systems to check (Please
      ensure your remote systems are scp command accessable)

      default is local system
    """

    if version:
        print(__VERSION__)
        exit()

    FORMAT = "%(asctime)-15s %(message)s"
    logging.basicConfig(format=FORMAT, handlers=[RichHandler()])
    logger = logging.getLogger("rich")
    logger.setLevel(logging.INFO)

    target = Check_Target(check_target)

    dst = Path(output)
    if dst.is_dir() or output.endswith("/"):
        dst = dst / "check_result"

    if not dst_is_ok(dst, out_format):
        logger.error("Can't write to output")
        exit(1)

    # try to guess format from file extension
    if out_format is None:
        ext_to_format = {v: k for k, v in FORMAT_TYPES.items()}
        out_format = ext_to_format.get(dst.suffix, None)

    if target.rpm:
        progress = Progress(
            "{task.description}",
            SpinnerColumn(),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        )
        with progress:
            rpm_check = terminal_logs.KMPProcessor(terminal_logs.KMPTerminalOutput(progress))
            check_result = rpm_check.process_kmp(target.rpm)

    elif target.dir:
        progress = Progress(
            "{task.description}",
            SpinnerColumn(),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        )
        with progress:
            log = KMPTerminalOutput(progress)
            df = analysis.kmps_to_dataframe(target.dir, log)
        reporter = KMPReporter()
        export(reporter, df, out_format, dst)
        logger.info(
            "[green]Check is completed![/]"
            "The result has been saved to "
            "[bold green]%s[/]" % dst,
            extra={"markup": True},
        )

    elif target.system:
        try:
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
        except socket.gaierror as e:
            logger.warning(f"Get ip by hostname: {hostname} failed: {e}")
            ip = "127.0.0.1"

        label = "%s (%s)" % (hostname, ip)
        logger.info("Retrieving kernel module data for %s" % label)
        reporter = KMReporter()
        export(reporter, label, out_format, dst)

    elif target.config is not None:
        servers = target.config["servers"]
        check_result = check_remote_servers(logger, servers)
        exporter = data_exporter.DriversExporter()
        export(exporter, check_result, out_format, dst)
        logger.info(
            "[green]Check is completed[/]"
            "Please see the results in [bold green]%s[/]" % dst.parent,
            extra={"markup": True},
        )


if __name__ == "__main__":
    run()
