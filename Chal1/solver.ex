defmodule Challenge do
  def loadfile(filename) do
    case File.read(filename) do
      {:ok, data} -> data
      {:error, _} -> IO.puts("Error reading from file: #{filename}")
    end
  end

  def solve_first() do
    "input"
    |> loadfile
    |> String.split()
    |> Enum.map(&String.to_integer/1)
    |> Enum.chunk_every(2)
    |> Enum.map(&List.to_tuple/1)
    |> Enum.unzip()
    |> sortlists
    |> solve
    |> Enum.sum()
    |> IO.inspect(label: "Total distance")
  end

  def sortlists({leftlist, rightlist}) do
    {Enum.sort(leftlist), Enum.sort(rightlist)}
  end

  def solve({leftlist, rightlist}) do
    Enum.zip_reduce(leftlist, rightlist, [], fn a, b, acc ->
      [abs(a - b) | acc]
    end)
    |> Enum.reverse()
  end
end

Challenge.solve_first()
