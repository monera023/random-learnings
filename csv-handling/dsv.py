from dataclasses import dataclass

class DSV():
    @property
    def delimiter(cls) -> bytes:
        return b'\x1F'

    @property
    def record_separator(cls) -> bytes:
        return b'\x1E'

    @property
    def encoding(cls) -> bytes:
        return 'utf-8'


@dataclass
class DSVWriter(DSV):
    output_file: str

    def write(self, data: list[list]) -> None:
        with open(self.output_file, 'wb') as file:
            for row in data:
                encoded_row = self.delimiter.join(
                    field.encode(self.encoding) for field in row
                )
                file.write(encoded_row + self.record_separator)


@dataclass
class DSVReader(DSV):
    input_file: str
    chunk_size: int = 1024
    _buffer: bytes = b""

    def read(self) -> None:
        with open(self.input_file, 'rb') as file:
            chunk = file.read(self.chunk_size)
            while chunk:
                self._buffer += chunk

                while self.record_separator in self._buffer:
                    record, self._buffer = self._buffer.split(self.record_separator, 1)
                    # Got one row here
                    fields = record.split(self.delimiter)
                    print([field.decode(self.encoding) for field in fields])
                chunk = file.read(self.chunk_size)
            # Process remaining data in _buffer
            if self._buffer:
                # Here data without any record_separator
                fields = record.split(self.delimiter)
                print([field.decode(self.encoding) for field in fields])
