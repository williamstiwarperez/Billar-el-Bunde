import {Link} from 'react-router-dom';

export function Navigation(){
    return(
    <div>
        <link to='/tasks'>
        <h1>tasks aPP</h1>
        </link>
        <Link to="/tasks-create">Create Task</Link>
    </div>
    )
}