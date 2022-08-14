# domains-blocker

### this script blocks domains on the computer

naturally the idea is not mine, I just implemented a well-known principle

## How it works

### example:

<pre>
object = DomainsBlocker([domain, ])                          # create a class object, a list of domains as a parameter
object = DomainsBlocker([domain, start_time, finish_time])   # create class object, list of domains and timeframe as parameters

object.start()                                               # execute the start method
</pre>
<br>

### setters:

<pre>
setdomain([domain,])
settimeframe(start_time, finish_time)
</pre>
