from dataclasses import dataclass as _dataclass
import enum as _enum
from typing import ClassVar as _ClassVar
import re as _re


class CompilationError(RuntimeError):
    pass


class EncodedPair:
    from typing import Optional as _Optional

    def __init__(self,
                 first: int,
                 second: int):
        self.__tuple: tuple[int, int] = first, second

        if any(element < 0 for element in self.__tuple):
            raise ValueError(f"{__class__.__name__} must be of non-negatives!")

    def encode(self) -> int:
        return (2 ** self[0]) * (2 * self[1] + 1) - 1

    def __getitem__(self,
                    index: int) -> int:
        return self.__tuple[index]

    def __int__(self) -> int:
        return self.encode()

    def __str__(self) -> str:
        return str(self.__tuple)

    def __eq__(self,
               other: _Optional["EncodedPair"]) -> bool:
        return other is not None and self.__tuple == other.__tuple

    @staticmethod
    def decode(pair_encoding: int) -> "EncodedPair":
        if pair_encoding < 0:
            raise ValueError(f"{__class__.__name__} encoding must be non-negative!")

        from sympy.ntheory import factorint
        pair_encoding += 1
        factorization: dict[int, int] = factorint(pair_encoding)
        return EncodedPair(factorization.get(2, 0),
                           ((pair_encoding // (2 ** factorization.get(2, 0))) - 1) // 2)


class EncodedList:
    from typing import Iterator as _Iterator, Optional as _Optional

    def __init__(self,
                 list_: list[int]):
        self.__list: list[int] = list_.copy()

        if any(element < 0 for element in self.__list):
            raise ValueError(f"{__class__.__name__} must be of non-negatives!")

    def encode(self) -> int:
        if len(self.__list) == 0:
            return 1

        from sympy.ntheory import primerange, prime

        mul: int = 1
        for p, exponent in zip(primerange(prime(len(self.__list)) + 1), self.__list):
            mul *= p ** exponent
        return mul

    def __getitem__(self,
                    index: int) -> int:
        return self.__list[index]

    def __setitem__(self,
                    index: int,
                    value: int) -> None:
        self.__list[index] = value

    def __int__(self) -> int:
        return self.encode()

    def __str__(self) -> str:
        return str(self.__list)

    def __eq__(self,
               other: _Optional["EncodedList"]) -> bool:
        return other is not None and self.__list == other.__list

    def __iter__(self) -> _Iterator[int]:
        return iter(self.__list)

    @staticmethod
    def decode(number: int) -> "EncodedList":
        if number < 1:
            raise ValueError(f"{__class__.__name__} encoding must be positive!")

        from sympy.ntheory import primerange, factorint

        factorization: dict[int, int] = factorint(number)
        return EncodedList([
            factorization.get(prime, 0)
            for prime in primerange(max(factorization, default=0) + 1)
        ])


@_dataclass(frozen=True)
class Variable:
    from typing import Optional as _Optional

    name: str
    index: int = 1
    _pattern: _ClassVar[_re.Pattern[str]] = _re.compile(r"\s*(?P<variable_name>[XYZ])(?P<index>([1-9][0-9]*)?)\s*",
                                                        flags=_re.IGNORECASE)

    def __post_init__(self) -> None:
        if self.name.upper() not in "XYZ":
            raise ValueError(f"{__class__.__name__} name must be X/Y/Z: '{self.name}'")
        if self.index < 1:
            raise ValueError(f"{__class__.__name__} index must be positive: {self.index}")
        if self.name.upper() == "Y" and self.index > 1:
            raise ValueError(f"{__class__.__name__} named 'Y' may only be of index 1")

    @staticmethod
    def compile(variable_string: str) -> "Variable":
        if variable_match := _re.fullmatch(Variable._pattern, variable_string):
            try:
                return Variable(
                    variable_match.group("variable_name"),
                    int(variable_match.group("index"))
                    if len(variable_match.group("index")) > 0
                    else
                    1
                )
            except ValueError as exception:
                raise CompilationError(str(exception))
        raise CompilationError(f"Failed to compile variable: \"{variable_string}\"")

    def encode(self) -> int:
        return (
            1
            if self.name.upper() == "Y"
            else
            (self.index * 2 + (0 if self.name.upper() == "X" else 1))
        )

    @staticmethod
    def decode(encoded_variable: int) -> "Variable":
        if encoded_variable < 1:
            raise ValueError(f"{__class__.__name__} encodings must be positive!")
        encoded_variable -= 1
        return (
            Variable("Y", 1)
            if encoded_variable == 0
            else
            Variable(
                "X"
                if encoded_variable % 2 != 0
                else
                "Z",
                ((encoded_variable - 1) // 2) + 1
            )
        )

    def __str__(self) -> str:
        return self.name + ("" if self.index == 1 else str(self.index))

    def __eq__(self,
               other: _Optional["Variable"]) -> bool:
        return other is not None and self.name.upper() == other.name.upper() and self.index == other.index

    def __hash__(self) -> int:
        return hash((self.name.upper(), self.index))


@_dataclass(frozen=True)
class Label:
    from typing import Optional as _Optional

    name: str
    index: int = 1
    _pattern: _ClassVar[_re.Pattern[str]] = _re.compile(r"\s*(?P<label>[A-E])(?P<index>([1-9][0-9]*)?)\s*",
                                                        flags=_re.IGNORECASE)

    def __post_init__(self) -> None:
        if self.name.upper() not in "ABCDE":
            raise ValueError(f"{__class__.__name__} must be of name A/B/C/D/E: '{self.name}'")
        if self.index < 1:
            raise ValueError(f"{__class__.__name__} index is not positive: {self.index}")

    @staticmethod
    def compile(label_string: str) -> "Label":
        if label_match := _re.fullmatch(Label._pattern, label_string):
            return Label(label_match.group("label"),
                         int(label_match.group("index"))
                         if len(label_match.group("index")) > 0
                         else
                         1)
        raise CompilationError(f"Failed to compile label: \"{label_string}\"")

    def encode(self) -> int:
        return (self.index - 1) * (ord("E") - ord("A") + 1) + (ord(self.name.upper()) - ord("A") + 1)

    @staticmethod
    def decode(encoded_label: int) -> "Label":
        if encoded_label < 1:
            raise ValueError(f"{__class__.__name__} encoding must be positive!")
        return Label(
            "ABCDE"[(encoded_label - 1) % len("ABCDE")],
            ((encoded_label - 1) // 5) + 1
        )

    def __str__(self) -> str:
        return f"{self.name}" + ("" if self.index == 1 else str(self.index))

    def __eq__(self,
               other: _Optional["Label"]) -> bool:
        return other is not None and self.name.upper() == other.name.upper() and self.index == other.index

    def __hash__(self) -> int:
        return hash((self.name.upper(), self.index))


class VariableCommandType(_enum.IntEnum):
    NoOp = 0
    Increment = 1
    Decrement = 2
    _ignore_ = ["_pattern"]
    _pattern: _re.Pattern

    @staticmethod
    def compile(command_type: str) -> "VariableCommandType":
        # noinspection PyTypeChecker
        if command_type_match := _re.fullmatch(VariableCommandType._pattern, command_type):
            return (
                VariableCommandType.Increment
                if command_type_match.group("operation") == '+'
                else
                VariableCommandType.Decrement
            )
        if _re.fullmatch(r"\s*", command_type):
            return VariableCommandType.NoOp

    def encode(self) -> int:
        # noinspection PyTypeChecker
        return int(self.value)

    @staticmethod
    def decode(encoded_variable_command_type: int) -> "VariableCommandType":
        return VariableCommandType(encoded_variable_command_type)

    def __str__(self) -> str:
        return (
            ""
            if self.value == VariableCommandType.NoOp
            else
            " + 1"
            if self.value == VariableCommandType.Increment
            else
            " - 1"
        )


VariableCommandType._pattern = _re.compile(r"(?P<operation>[+-])\s*1")


@_dataclass(frozen=True, eq=True)
class VariableCommand:
    variable: Variable
    command_type: VariableCommandType

    _variable_pattern: _ClassVar[_re.Pattern[str]] = _re.compile(r"\s*(?P<variable>[XYZ]([1-9][0-9]*)?)\s*<\s*-"
                                                                 r"\s*(?P=variable)\s*(?P<operation>([+-]\s*1)?)\s*",
                                                                 flags=_re.IGNORECASE)

    @staticmethod
    def compile(variable_command: str) -> "VariableCommand":
        if variable_match := _re.fullmatch(VariableCommand._variable_pattern, variable_command):
            return VariableCommand(Variable.compile(variable_match.group("variable")),
                                   VariableCommandType.compile(variable_match.group("operation")))
        raise CompilationError(f"Failed to compile variable command: \"{variable_command}\"")

    def encode_repr(self) -> tuple[int, int]:
        return (
            self.command_type.encode(),
            self.variable.encode() - 1
        )

    @staticmethod
    def decode_repr(repr_: tuple[int, int]) -> "VariableCommand":
        command_type, variable_encoding = repr_
        if command_type > 2:
            raise ValueError(f"{__class__.__name__} encoding first element must be less than or equal to 2: {repr_}")
        return VariableCommand(
            Variable.decode(variable_encoding + 1),
            VariableCommandType.decode(command_type)
        )

    def encode(self) -> int:
        return EncodedPair(*self.encode_repr()).encode()

    @staticmethod
    def decode(encoded_sentence: int) -> "VariableCommand":
        if encoded_sentence < 0:
            raise ValueError(f"{__class__.__name__} encoding must be non-negative!")
        return VariableCommand.decode_repr(tuple(EncodedPair.decode(encoded_sentence)))

    def __str__(self) -> str:
        return (
            f"{str(self.variable)} <- {str(self.variable)}{str(self.command_type)}"
        )


@_dataclass(frozen=True, eq=True)
class JumpCommand:
    variable: Variable
    label: Label

    _jump_pattern: _ClassVar[_re.Pattern[str]] = _re.compile(r"\s*IF\s+(?P<variable>[XYZ]([1-9][0-9]*)?)\s*!\s*=\s*0\s+"
                                                             r"GOTO\s+(?P<label>[A-E]([1-9][0-9]*)?)\s*",
                                                             flags=_re.IGNORECASE)

    @staticmethod
    def compile(jump_command: str) -> "JumpCommand":
        if jump_match := _re.fullmatch(JumpCommand._jump_pattern, jump_command):
            return JumpCommand(Variable.compile(jump_match.group("variable")),
                               Label.compile(jump_match.group("label")))
        raise CompilationError(f"Failed to compile jump command: \"{jump_command}\"")

    def encode_repr(self) -> tuple[int, int]:
        return (
            self.label.encode() + 2,
            self.variable.encode() - 1
        )

    @staticmethod
    def decode_repr(repr_: tuple[int, int]) -> "JumpCommand":
        command_type, variable_encoding = repr_
        if command_type <= 2:
            raise ValueError(f"{__class__.__name__} encoding first element must be greater than 2: {repr_}")
        return JumpCommand(
            Variable.decode(variable_encoding + 1),
            Label.decode(command_type - 2)
        )

    def encode(self) -> int:
        return EncodedPair(*self.encode_repr()).encode()

    @staticmethod
    def decode(encoded_sentence: int) -> "JumpCommand":
        if encoded_sentence < 0:
            raise ValueError(f"{__class__.__name__} encoding must be non-negative!")
        return JumpCommand.decode_repr(tuple(EncodedPair.decode(encoded_sentence)))

    def __str__(self) -> str:
        return f"IF {str(self.variable)} != 0 GOTO {str(self.label)}"


@_dataclass(frozen=True, eq=True)
class Sentence:
    from typing import Union as _Union

    command: _Union[JumpCommand, VariableCommand]

    @staticmethod
    def compile(sentence: str) -> "Sentence":
        try:
            return Sentence(JumpCommand.compile(sentence))
        except CompilationError:
            pass

        try:
            return Sentence(VariableCommand.compile(sentence))
        except CompilationError:
            pass

        raise CompilationError(f"Failed to compile sentence: \"{sentence}\"")

    def encode_repr(self) -> tuple[int, int]:
        return self.command.encode_repr()

    @staticmethod
    def decode_repr(repr_: tuple[int, int]) -> "Sentence":
        command_type, variable_encoding = repr_
        return Sentence(
            JumpCommand.decode_repr((command_type, variable_encoding))
            if command_type > 2
            else
            VariableCommand.decode_repr((command_type, variable_encoding))
        )

    def encode(self) -> int:
        return self.command.encode()

    @staticmethod
    def decode(encoded_sentence: int) -> "Sentence":
        if encoded_sentence < 0:
            raise ValueError(f"{__class__.__name__} encoding must be non-negative!")
        return Sentence.decode_repr(tuple(EncodedPair.decode(encoded_sentence)))

    def __str__(self) -> str:
        return str(self.command)


@_dataclass(frozen=True, eq=True)
class Instruction:
    from typing import Optional as _Optional

    sentence: Sentence
    label: _Optional[Label] = None

    _pattern: _ClassVar[_re.Pattern[str]] = _re.compile(r"\s*(\[\s*(?P<label>[A-E]([1-9][0-9]*)?)\s*])?"
                                                        r"\s*(?P<sentence>.*)\s*",
                                                        flags=_re.IGNORECASE)

    @staticmethod
    def compile(line: str) -> "Instruction":
        if not (instruction_match := _re.fullmatch(Instruction._pattern, line)):
            raise CompilationError(f"Failed to compile instruction: \"{line}\"")
        return Instruction(Sentence.compile(instruction_match.group("sentence")),
                           Label.compile(label)
                           if (label := instruction_match.group("label"))
                           else
                           None)

    def encode_repr(self) -> tuple[int, tuple[int, int]]:
        return (
            0
            if self.label is None
            else
            self.label.encode(),
            self.sentence.encode_repr()
        )

    @staticmethod
    def decode_repr(repr_: tuple[int, tuple[int, int]]) -> "Instruction":
        label_encoding, sentence_encoding = repr_
        return Instruction(
            Sentence.decode_repr(sentence_encoding),
            Label.decode(label_encoding)
            if label_encoding != 0
            else
            None
        )

    def encode(self) -> int:
        encoding: tuple[int, tuple[int, int]] = self.encode_repr()
        return EncodedPair(encoding[0], EncodedPair(*encoding[1]).encode()).encode()

    @staticmethod
    def decode(encoded_instruction: int) -> "Instruction":
        if encoded_instruction < 0:
            raise ValueError(f"{__class__.__name__} encoding must be non-negative!")

        label_encoding, sentence_encoding = EncodedPair.decode(encoded_instruction)
        return Instruction.decode_repr((label_encoding, tuple(EncodedPair.decode(sentence_encoding))))

    def __str__(self) -> str:
        return (f"[{str(self.label)}] " if self.label is not None else "") + str(self.sentence)


_program_recursion_depth: int = 0


@_dataclass(frozen=True, eq=True)
class Program:
    from typing import Optional as _Optional

    instructions: list[Instruction]
    _labeled_sugar_pattern: _ClassVar[_re.Pattern[str]] = _re.compile(r"\s*\[\s*(?P<sugar_label>"
                                                                      r"[A-E]([1-9][0-9]*)?)\s*].*",
                                                                      flags=_re.IGNORECASE)
    _label_length_pattern: _ClassVar[_re.Pattern[str]] = _re.compile(r"(\[.*])?\s*")

    def __post_init__(self) -> None:
        if (len(self.instructions) > 0 and
                self.instructions[-1].label is None and
                type(self.instructions[-1].sentence.command) is VariableCommand and
                self.instructions[-1].sentence.command.variable.name.upper() == "Y" and
                self.instructions[-1].sentence.command.command_type == VariableCommandType.NoOp):
            raise ValueError("Convention of Y<-Y is not respected!")

    @_dataclass
    class _SugarJob:
        sugar: "SyntacticSugar"
        sugar_invocation: str
        index_to_inject: int

    @staticmethod
    def __update_by_instruction(used_labels: set[Label],
                                used_variables: set[Variable],
                                *instructions_: Instruction) -> None:
        for instruction in instructions_:
            used_variables.add(instruction.sentence.command.variable)

            if instruction.label is not None:
                used_labels.add(instruction.label)

            if type(instruction.sentence.command) is JumpCommand:
                used_labels.add(instruction.sentence.command.label)

    @staticmethod
    def __create_sugar_job(line: str,
                           sugars: list["SyntacticSugar"],
                           instructions: list[Instruction],
                           used_variables: set[Variable],
                           used_labels: set[Label]) -> _Optional[_SugarJob]:
        if (sugar := next((sugar for sugar in sugars if sugar.validate(line)), None)) is not None:
            for parameter in sugar.parameters(line):
                if type(parameter) is Label:
                    used_labels.add(parameter)
                elif type(parameter) is Variable:
                    used_variables.add(parameter)
            if label_match := _re.fullmatch(Program._labeled_sugar_pattern, line):
                used_labels.add(new_label := Label.compile(label_match.group("sugar_label")))
                instructions.append(Instruction(Sentence(VariableCommand(Variable("Y"),
                                                                         VariableCommandType.NoOp)),
                                                new_label))
            return Program._SugarJob(sugar, line, len(instructions))

    @_dataclass
    class _ProgramParseResult:
        instructions: list[Instruction]
        sugar_jobs: list["Program._SugarJob"]
        used_variables: set[Variable]
        used_labels: set[Label]

    @staticmethod
    def _parse(*program: str,
               sugars: list["SyntacticSugar"]) -> _ProgramParseResult:
        from typing import Optional
        parse_result: Program._ProgramParseResult = Program._ProgramParseResult([], [], set(), set())

        for line in program:
            try:
                parse_result.instructions.append(Instruction.compile(line))
                Program.__update_by_instruction(parse_result.used_labels,
                                                parse_result.used_variables,
                                                parse_result.instructions[-1])
            except CompilationError as compilation_failure:
                sugar_job: Optional[Program._SugarJob] = Program.__create_sugar_job(line,
                                                                                    sugars,
                                                                                    parse_result.instructions,
                                                                                    parse_result.used_variables,
                                                                                    parse_result.used_labels)
                if sugar_job is None:
                    raise compilation_failure
                parse_result.sugar_jobs.append(sugar_job)
        return parse_result

    @staticmethod
    def _expand_program(program_parse_result: _ProgramParseResult,
                        verbose: bool = False) -> None:
        for sugar_job_index, sugar_job in enumerate(program_parse_result.sugar_jobs):
            if verbose:
                print("| " * (_program_recursion_depth - 1) + f"Compiling '{sugar_job.sugar_invocation}' "
                                                              f"('{sugar_job.sugar.title}')")
            instructions_to_inject: list[Instruction] = sugar_job.sugar.compile(sugar_job.sugar_invocation,
                                                                                program_parse_result.used_labels,
                                                                                program_parse_result.used_variables,
                                                                                verbose).instructions
            Program.__update_by_instruction(program_parse_result.used_labels,
                                            program_parse_result.used_variables,
                                            *instructions_to_inject)
            for instruction_index, instruction_to_inject in enumerate(instructions_to_inject):
                program_parse_result.instructions.insert(sugar_job.index_to_inject + instruction_index,
                                                         instruction_to_inject)
            sugar_job_index += 1
            while sugar_job_index < len(program_parse_result.sugar_jobs):
                program_parse_result.sugar_jobs[sugar_job_index].index_to_inject += len(instructions_to_inject)
                sugar_job_index += 1

    @staticmethod
    def compile(*program: str,
                sugars: _Optional[list["SyntacticSugar"]] = None,
                verbose: bool = False) -> "Program":
        global _program_recursion_depth
        _program_recursion_depth += 1

        try:
            program_parse_result: Program._ProgramParseResult = Program._parse(*program,
                                                                               sugars=[] if sugars is None else sugars)
            Program._expand_program(program_parse_result, verbose)

            try:
                return Program(program_parse_result.instructions)
            except ValueError as exception:
                raise CompilationError(str(exception))
        finally:
            _program_recursion_depth -= 1

    def encode_repr(self) -> list[tuple[int, tuple[int, int]]]:
        return [
            instruction.encode_repr()
            for instruction in self.instructions
        ]

    @staticmethod
    def decode_repr(repr_: list[tuple[int, tuple[int, int]]]) -> "Program":
        return Program(
            [
                Instruction.decode_repr(instruction_encoding)
                for instruction_encoding in repr_
            ]
        )

    def encode(self) -> int:
        return EncodedList([instruction.encode() for instruction in self.instructions]).encode() - 1

    @staticmethod
    def decode(encoded_program: int) -> "Program":
        if encoded_program < 0:
            raise ValueError(f"{__class__.__name__} encoding must be non-negative!")

        return Program(
            [
                Instruction.decode(instruction_encoding)
                for instruction_encoding in EncodedList.decode(encoded_program + 1)
            ]
        )

    def __add__(self,
                other: "Program") -> "Program":
        return Program(self.instructions + other.instructions)

    def __str__(self) -> str:
        max_sentence_indentation: int = max(
            (
                len(_re.match(Program._label_length_pattern, str(instruction)).group())
                for instruction in self.instructions
            ),
            default=0
        )

        return "\n".join(
            (start := _re.match(Program._label_length_pattern, str(instruction)).group()) +
            (max_sentence_indentation - len(start)) * " " +
            str(instruction.sentence)
            for instruction in self.instructions
        )


@_dataclass(frozen=True, eq=True)
class Const:
    value: int

    @staticmethod
    def compile(const: str) -> "Const":
        try:
            return Const(int(const))
        except ValueError:
            raise CompilationError(f"Failed to compile const: {const}")

    def __str__(self) -> str:
        return str(self.value)


class SyntacticSugar:
    from typing import (
        Optional as _Optional,
        Union as _Union,
        Type as _Type
    )

    _special_chars_pattern: _re.Pattern[str] = _re.compile(r"(?P<special_char>[*+\-|^\\&~#])")

    _supported_types_patterns: dict[_Union[_Type[Label], _Type[Variable], _Type[Const]], str] = {
        Label: r"[A-E]([1-9][0-9]*)?",
        Variable: r"[XYZ]([1-9][0-9]*)?",
        Const: r"(([1-9][0-9]*)|0)"
    }

    _supported_types_regex_group: str = (
        r"(" +
        r"|".join(actual_type.__name__ for actual_type in _supported_types_patterns) +
        r")"
    )

    _sugar_arguments_pattern: _re.Pattern[str] = _re.compile(
        r"{\s*(?P<type>" + _supported_types_regex_group + r")\s+" +
        r"(?P<variable_name>[A-Z]([A-Z]|\d)*)\s*}",
        flags=_re.IGNORECASE
    )

    _back_reference_pattern: _re.Pattern[str] = _re.compile(
        r"{\s*" +
        _supported_types_regex_group +
        r"\s+"
        r"(?P<argument_name>[A-Z]([A-Z]|\d)*)\s*}",
        flags=_re.IGNORECASE
    )

    def __create_sugar_args_dict(self,
                                 usage: str) -> None:
        from typing import Type, Union

        self.__argument_name_to_type: dict[str, Union[Type[Const], Type[Variable], Type[Label]]] = {}
        for match in _re.finditer(SyntacticSugar._sugar_arguments_pattern, usage):
            variable_name: str = match.group("variable_name").upper()
            variable_type: Union[Type[Const], Type[Label], Type[Variable]] = {
                supported_type.__name__.lower(): supported_type
                for supported_type in SyntacticSugar._supported_types_patterns
            }[match.group("type").lower()]

            if variable_name in self.__argument_name_to_type:
                if self.__argument_name_to_type[variable_name] != variable_type:
                    raise ValueError(f"Sugar back-reference does not maintain the same type "
                                     f"({self.__argument_name_to_type[variable_name]} != {variable_type})")
            else:
                self.__argument_name_to_type[variable_name] = variable_type

    def __create_invocation_regex(self,
                                  usage: str) -> None:
        for invocation_argument, supported_type in self.__argument_name_to_type.items():
            usage = _re.sub(r"{\s*" + supported_type.__name__ + r"\s+" +
                            invocation_argument + r"\s*}",
                            r"(?P<" + invocation_argument + r">" +
                            SyntacticSugar._supported_types_patterns[supported_type] + r")",
                            usage,
                            count=1,
                            flags=_re.IGNORECASE)
        usage = _re.sub(SyntacticSugar._back_reference_pattern,
                        r"(?P=\g<argument_name>)",
                        usage)

        if _re.search(r"[{}]", usage):
            raise ValueError(f"Invalid sugar usage title: {self.__title}")

        usage = r"\s*(\[[A-E]([1-9][0-9]*)?\])?\s*" + _re.sub(r"\s+", r"\\s*", usage) + r"\s*"

        self.__invocation_regex: _re.Pattern[str] = _re.compile(usage, flags=_re.IGNORECASE)

    def __set_implementation(self,
                             implementation: tuple[str, ...]) -> None:
        repeat_counter: int = 0
        for line in implementation:
            if (match := _re.fullmatch(r"\s*{\s*REPEAT\s+(?P<const_name>[A-Z]([A-Z]|\d)*)\s*}\s*",
                                       line,
                                       flags=_re.IGNORECASE)):
                if match.group("const_name") not in self.__argument_name_to_type:
                    raise ValueError(f"Unknown const '{match.group('const_name')}' used in repeat!")
                if self.__argument_name_to_type[match.group("const_name")] is not Const:
                    raise ValueError(f"'{match.group('const_name')}' used in repeat but isn't const!")
                repeat_counter += 1
            elif _re.fullmatch(r"\s*{\s*END\s+REPEAT\s*}\s*",
                               line,
                               flags=_re.IGNORECASE):
                if repeat_counter == 0:
                    raise ValueError("No 'REPEAT' for matching 'END REPEAT'!")
                repeat_counter -= 1
        if repeat_counter > 0:
            raise ValueError("No 'END REPEAT' for matching 'REPEAT'!")

        self.__implementation: tuple[str] = implementation

    def __init__(self,
                 usage: str,
                 *implementation: str,
                 sugars: _Optional[list["SyntacticSugar"]] = None):
        self.__title: str = usage
        self.__sugars: list[SyntacticSugar] = [] if sugars is None else sugars

        usage = _re.sub(SyntacticSugar._special_chars_pattern, r"\\\g<special_char>", usage.strip())
        self.__create_sugar_args_dict(usage)
        self.__create_invocation_regex(usage)
        self.__set_implementation(implementation)

    class _VariableGenerator:
        def __init__(self,
                     other_variables: set[Variable]):
            self.__unused_variable_index: int = max((variable.index
                                                     for variable in other_variables),
                                                    default=0) + 1

        def generate(self,
                     starting_index: int = 0) -> Variable:
            variable: Variable = Variable("Z", starting_index + self.__unused_variable_index)
            self.__unused_variable_index += 1
            return variable

    class _LabelGenerator:
        def __init__(self,
                     other_labels: set[Label]):
            self.__unused_label_index: int = max((label.index for label in other_labels),
                                                 default=0) + 1

        def generate(self,
                     starting_index: int = 0) -> Label:
            label: Label = Label("A", starting_index + self.__unused_label_index)
            self.__unused_label_index += 1
            return label

    class _ProgramFixer:
        from typing import (
            Union as _Union,
            Optional as _Optional
        )

        def __used_labels_and_variables(self,
                                        used_labels: _Optional[set[Label]],
                                        used_variables: _Optional[set[Variable]]) -> tuple[set[Label], set[Variable]]:
            used_labels = set() if used_labels is None else used_labels
            used_variables = set() if used_variables is None else used_variables
            used_label_params: set[Label] = set()
            used_variable_params: set[Variable] = set()

            for parameter in self.__parameters:
                if type(parameter) is Label and parameter not in used_labels:
                    used_label_params.add(parameter)
                elif type(parameter) is Variable and parameter not in used_variables:
                    used_variable_params.add(parameter)
            if len(used_label_params) > 0:
                used_labels = used_labels.union(used_label_params)
            if len(used_variable_params) > 0:
                used_variables = used_variables.union(used_variable_params)

            return used_labels, used_variables

        def __init__(self,
                     parameters: list[_Union[Label, Variable]],
                     used_labels: _Optional[set[Label]],
                     used_variables: _Optional[set[Variable]]):
            from typing import Union

            self.__parameters: list[Union[Label, Variable]] = parameters
            used_labels, used_variables = self.__used_labels_and_variables(used_labels, used_variables)

            self.__variable_generator: SyntacticSugar._VariableGenerator = (
                SyntacticSugar._VariableGenerator(used_variables)
            )
            self.__label_generator: SyntacticSugar._LabelGenerator = SyntacticSugar._LabelGenerator(
                used_labels
            )
            self.__fixes_to_perform: dict[Union[Label, Variable], Union[Label, Variable]] = {}
            self.__parameter_replacements: dict[str, str] = {}

        def process_parameter_fixes(self) -> None:
            max_sugar_internals: int = 1000000000000000
            # Code smell due to the way the algorithm works with the sugar arguments (replacing them at the start
            # and fixing them later alongside the other variables)

            for parameter in self.__parameters:
                generated: type(parameter) = (
                    self.__label_generator
                    if type(parameter) is Label
                    else
                    self.__variable_generator
                ).generate(max_sugar_internals)
                self.__parameter_replacements[str(parameter)]: str = str(generated)
                self.__fixes_to_perform[generated] = parameter

        def process_program_fixes(self,
                                  program: Program) -> None:
            for instruction in program.instructions:
                if (
                    instruction.label is not None and
                    instruction.label not in self.__fixes_to_perform
                ):
                    self.__fixes_to_perform[instruction.label] = self.__label_generator.generate()
                if (
                    type(instruction.sentence.command) is JumpCommand and
                    instruction.sentence.command.label not in self.__fixes_to_perform
                ):
                    self.__fixes_to_perform[instruction.sentence.command.label] = self.__label_generator.generate()
                if (
                    instruction.sentence.command.variable.name.upper() not in {"X", "Y"} and
                    instruction.sentence.command.variable not in self.__fixes_to_perform
                ):
                    self.__fixes_to_perform[instruction.sentence.command.variable] = (
                        self.__variable_generator.generate()
                    )

        def parameter_replacement(self,
                                  parameter: str) -> str:
            return self.__parameter_replacements.get(parameter, parameter)

        def __fix(self,
                  entity: _Union[Label, Variable]) -> _Union[Label, Variable]:
            return self.__fixes_to_perform.get(entity, entity)

        def fix_program(self,
                        program: Program) -> Program:
            return Program([
                    Instruction(
                        Sentence(
                            JumpCommand(self.__fix(instruction.sentence.command.variable),
                                        self.__fix(instruction.sentence.command.label))
                            if type(instruction.sentence.command) is JumpCommand
                            else
                            VariableCommand(self.__fix(instruction.sentence.command.variable),
                                            instruction.sentence.command.command_type)
                        ),
                        self.__fix(instruction.label)
                    )
                    for instruction in program.instructions
                ])

    def validate(self,
                 invocation: str) -> bool:
        return bool(_re.fullmatch(self.__invocation_regex, invocation))

    @property
    def title(self) -> str:
        return self.__title

    def __str__(self) -> str:
        return self.__title

    def __generate_instructions(self,
                                invocation_match: _re.Match,
                                code_fixer: _ProgramFixer) -> list[str]:
        sugar_program_instructions: list[str] = []
        repeat_counters: list[int] = []
        repeat_start_indices: list[int] = []
        line_index: int = 0

        while line_index < len(self.__implementation):
            if repeat_match := _re.fullmatch(r"\s*{\s*REPEAT\s+(?P<const_name>[A-Z]([A-Z]|\d)*)\s*}\s*",
                                             self.__implementation[line_index],
                                             flags=_re.IGNORECASE):
                line_index += 1
                repeat_counters.append(int(invocation_match.group(repeat_match.group("const_name"))))
                repeat_start_indices.append(line_index)
            elif _re.fullmatch(r"\s*{\s*END\s+REPEAT\s*}\s*",
                               self.__implementation[line_index],
                               flags=_re.IGNORECASE):
                repeat_counters[-1] -= 1
                if repeat_counters[-1] <= 0:
                    repeat_counters.pop()
                    repeat_start_indices.pop()
                    line_index += 1
                else:
                    line_index = repeat_start_indices[-1]
            elif len(repeat_counters) == 0 or repeat_counters[-1] > 0:
                line: str = self.__implementation[line_index]
                for invocation_argument_name, invocation_argument_type in self.__argument_name_to_type.items():
                    line = _re.sub(r"{\s*" + invocation_argument_name + r"\s*}",
                                   code_fixer.parameter_replacement(
                                       invocation_match.group(invocation_argument_name)
                                   ),
                                   line,
                                   flags=_re.IGNORECASE)
                sugar_program_instructions.append(line)
                line_index += 1
            else:
                line_index += 1

        return sugar_program_instructions

    def compile(self,
                invocation: str,
                used_labels: _Optional[set[Label]] = None,
                used_variables: _Optional[set[Variable]] = None,
                verbose: bool = False) -> Program:
        if (invocation_match := _re.fullmatch(self.__invocation_regex, invocation)) is None:
            raise CompilationError(f"Failed using sugar {self.__title} to compile line: '{invocation}'")

        program_fixer: SyntacticSugar._ProgramFixer = SyntacticSugar._ProgramFixer(
            [
                parameter for parameter in self.__parameters(invocation_match)
                if type(parameter) is not Const
            ],
            used_labels,
            used_variables
        )

        program_fixer.process_parameter_fixes()

        sugar_program: Program = Program.compile(*self.__generate_instructions(invocation_match, program_fixer),
                                                 sugars=self.__sugars,
                                                 verbose=verbose)
        program_fixer.process_program_fixes(sugar_program)
        return program_fixer.fix_program(sugar_program)

    def __parameters(self,
                     invocation_match: _re.Match) -> set[_Union[Label, Variable, Const]]:
        return {
            invocation_argument_type.compile(invocation_match.group(invocation_argument_name))
            for invocation_argument_name, invocation_argument_type in self.__argument_name_to_type.items()
        }

    def parameters(self,
                   invocation: str) -> set[_Union[Label, Variable, Const]]:
        if invocation_match := _re.fullmatch(self.__invocation_regex, invocation):
            return self.__parameters(invocation_match)
        raise CompilationError(f"Failed to determine sugar parameters of: '{invocation}'")


def compile_slang_file(slang_file_path: str,
                       verbose: bool = False) -> Program:
    with open(slang_file_path, "r") as file_to_compile:
        file_to_compile_content: list[str] = file_to_compile.readlines()

    current_section_lines: list[str] = []
    current_section_title: str = ""
    sugars: list[SyntacticSugar] = []
    is_main: bool = False
    is_before_first_sugar: bool = True

    for line_index, line in enumerate(file_to_compile_content):
        if _re.fullmatch(r"\s*(#(\s|.)*)?\s*", line):
            pass
        elif title_match := _re.fullmatch(r"\s*>\s*(?P<title>.*)\s*", line):
            if is_main:
                raise CompilationError(f"Encountered sugar title after MAIN: '{line}'")

            if is_before_first_sugar:
                is_before_first_sugar = False
            else:
                try:
                    sugars.append(SyntacticSugar(current_section_title,
                                                 *current_section_lines,
                                                 sugars=sugars.copy()))
                except ValueError as exception:
                    raise CompilationError(str(exception))
            is_main = bool(_re.fullmatch(r"\s*MAIN\s*",
                                         current_section_title := title_match.group("title").split("#")[0].strip(),
                                         _re.IGNORECASE))
            current_section_lines = []
        elif line_match := _re.fullmatch(r"\s*(?P<line>.*)\s*", line):
            current_section_lines.append(line_match.group("line").split("#")[0].strip())
        else:
            raise CompilationError(f"Failed to compile line {line_index}: '{line}'")

    if not is_main:
        raise CompilationError("Nonexistent 'MAIN' section!")

    return Program.compile(*current_section_lines,
                           sugars=sugars,
                           verbose=verbose)


def main() -> None:
    from argparse import ArgumentParser, Namespace
    from time import time

    argument_parser: ArgumentParser = ArgumentParser(description="S Compiler")
    input_source_group = argument_parser.add_mutually_exclusive_group(required=True)
    input_source_group.add_argument("-f",
                                    "--file",
                                    type=str,
                                    default=None,
                                    help="File to compile")
    input_source_group.add_argument("-d",
                                    "--decode",
                                    type=int,
                                    default=None,
                                    help="The program encoding")
    compiler_output = argument_parser.add_mutually_exclusive_group(required=True)
    compiler_output.add_argument("-o",
                                 "--output",
                                 type=str,
                                 help="Output binary file",
                                 default=None)
    compiler_output.add_argument("-e",
                                 "--encode",
                                 action="store_true",
                                 help="If present, print out the encoding of the program.\n"
                                      "NOTE: DO NOT use this flag for large binaries as it can "
                                      "result in IMPOSSIBLY SLOW calculations")
    compiler_output.add_argument("-p",
                                 "--print",
                                 action="store_true",
                                 help="If present, simply print out the compiled output")
    argument_parser.add_argument("-v",
                                 "--verbose",
                                 action="store_true",
                                 help="If present, print additional verbose compilation info")
    arguments: Namespace = argument_parser.parse_args()

    start_time: float = time()
    compiled_program: Program = (
        compile_slang_file(arguments.file, arguments.verbose)
        if arguments.decode is None
        else
        Program.decode(arguments.decode)
    )

    time_taken_to_compile: float = time() - start_time

    if arguments.verbose and arguments.file is not None:
        print()
    print(f"Finished compiling program (took {time_taken_to_compile:0.2f} seconds).")

    if arguments.output or arguments.print:
        program: str = str(compiled_program)
        if arguments.output:
            with open(arguments.output, "w") as output_file:
                output_file.write(program)

            print(f"Saved to binary: \"{arguments.output}\"")
        else:
            print(f"\n"
                  f"The Program:\n"
                  f"{program}")
    elif arguments.encode:
        print(f"It encodes to the value of {compiled_program.encode()}.")


if __name__ == '__main__':
    main()

__all__ = (
    "CompilationError",
    "EncodedPair",
    "EncodedList",
    "Variable",
    "Label",
    "JumpCommand",
    "VariableCommandType",
    "VariableCommand",
    "Sentence",
    "Instruction",
    "Program",
    "SyntacticSugar",
    "compile_slang_file",
    "main"
)
