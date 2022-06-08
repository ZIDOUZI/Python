in100 = {"a", "b", "c"}
in200 = {"a", "b", "d", "e", "f"}
in400 = {"b", "c", "d", "g", "h"}

in100and200 = in100 & in200
in100and400 = in100 & in400
in200and400 = in200 & in400
inAll = in100 & in200 & in400

inAny2 = (in100and200 | in100and400 | in200and400) - inAll
print(inAny2)
