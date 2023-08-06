from nginx_logs_parser_and_process.domain.Server.FilesSynchronizationError import FilesSynchronizationError
from nginx_logs_parser_and_process.domain.Server.Server import Server
import sysrsync


class SynchronizeRemoteNginxLogsWithLocalRepository:
    @staticmethod
    def process(source_server: Server, destination_server: Server) -> None:
        try:
            sysrsync.run(
                source=source_server.source_path,
                source_ssh=source_server.host,
                destination=destination_server.source_path,
                destination_ssh=destination_server.host,
                options=["-a"],
            )
        except Exception as error:
            raise FilesSynchronizationError(
                f"Files synchronization failed with source: {source_server.host}:{source_server.source_path} "
                f"and destination {destination_server.host}:{destination_server.source_path}. Exception: {error}"
            )
