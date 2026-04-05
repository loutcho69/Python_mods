from abc import ABC, abstractmethod
from typing import Any, Union
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._rank: int = 0
        self.processed_count: int = 0
        self.processor_name: str = ""

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        rank, value = self._storage.pop(0)
        return (rank, value)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.processor_name = "NumericProcessor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(
                not isinstance(item, bool) and isinstance(item, (int, float))
                for item in data
            )
        return False

    def ingest(self, data: Union[int, float, list[Union[int, float]]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append((self._rank, str(item)))
            self._rank += 1
            self.processed_count += 1


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.processor_name = "TextProcessor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: Union[str, list[str]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper text data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append((self._rank, item))
            self._rank += 1
            self.processed_count += 1


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.processor_name = "LogProcessor"

    def validate(self, data: Any) -> bool:
        def is_valid_log(d: Any) -> bool:
            return (isinstance(d, dict)
                    and all(isinstance(k, str) and isinstance(v, str)
                            for k, v in d.items()))
        if is_valid_log(data):
            return True
        if isinstance(data, list):
            return all(is_valid_log(item) for item in data)
        return False

    def ingest(self, data: Union[dict[str, str],
               list[dict[str, str]]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            log_level = item.get("log_level", "UNKNOWN")
            log_message = item.get("log_message", str(item))
            entry = f"{log_level}: {log_message}"
            self._storage.append((self._rank, entry))
            self._rank += 1
            self.processed_count += 1


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []
        self._total_received: int = 0
        self._unhandled_count: int = 0

    def register_processor(self, proc: DataProcessor) -> None:
        if not isinstance(proc, DataProcessor):
            raise TypeError(
                f"Expected a DataProcessor instance got {type(proc)}")
        self._processors.append(proc)
        print(f"Registered: {proc.processor_name}")

    def process_stream(self, stream: list[typing.Any]) -> None:
        print(f"\n{'─' * 55}")
        print(f"Processing stream of {len(stream)} element(s) …")
        print(f"{'─' * 55}")

        for index, element in enumerate(stream):
            self._total_received += 1
            handled = False

            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break

            if not handled:
                self._unhandled_count += 1
                print(
                    f"  [ERROR] No registered processor can handle element "
                    f"at index {index}: {element!r}"
                    f" (type={type(element).__name__})"
                )

        print(f"{'─' * 55}\n")

    def print_processors_stats(self) -> None:
        total_handled = self._total_received - self._unhandled_count

        print("=" * 55)
        print("  DATASTREAM STATISTICS")
        print("=" * 55)
        print(f"  {'Total elements received':<30} {self._total_received:>6}")
        print(f"  {'Total elements handled':<30} {total_handled:>6}")
        print(f"  {'Total elements unhandled':<30} {self._unhandled_count:>6}")
        print(f"  {'─' * 38}")
        print(f"  {'Processor':<28} {'Handled':>8}")
        print(f"  {'─' * 38}")

        for proc in self._processors:
            print(f"  {proc.processor_name:<28} {proc.processed_count:>8}")

        print("=" * 55)


def test() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    ds = DataStream()
    print("\n── Registering processors")
    ds.register_processor(NumericProcessor())
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    sample_stream: list[typing.Any] = [
        42,
        3.14159,
        "hello world",
        True,
        False,
        [1, 2, 3],
        {"name": "Alice", "age": 30},
        -7,
        0.001,
        "DataStream",
        None,
        [True, "x"],
        99,
    ]

    ds.process_stream(sample_stream)
    ds.print_processors_stats()


if __name__ == "__main__":
    test()
