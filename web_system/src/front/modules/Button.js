import React from 'react';

export default function Button({callback = f => f, enabled = true, label = ''}) {
    if(enabled === true)
        return <button onClick={callback}>{label}</button>
    else
        return <button onClick={callback} disabled>{label}</button>
}
